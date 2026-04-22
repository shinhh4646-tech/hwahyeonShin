"""
[Handover: Backend Detection Engine]
이 모듈은 bot_detection_logic.sql에 정의된 13가지 봇 감지 로직을 Python으로 구현한 핵심 엔진입니다.
- 각 메서드는 SQL 시나리오의 공식 명칭을 사용하여 설계되었습니다.
"""
from datetime import timedelta

class ASnapEngine:
    def __init__(self):
        # SQL 로직에 정의된 기준치들 (Thresholds)
        self.config = {
            'burst_actions_registration': 50,  # 1. High activity after reg
            'ip_duplication_limit': 5,         # 2. IP Address duplication
            'spam_keywords': ['gambling', 'ads', 'link'], # 3. Spam keyword
            'burst_post_limit': 100,           # 4. Burst posting
            'follow_limit': 1000,              # 5. Abnormal Follow ratio
            'comment_repeat_limit': 10,        # 6. Comment spamming
            'burst_comment_limit': 100,        # 7. High-speed commenting
            'burst_like_limit': 100,           # 8. High-speed liking
            'auto_reaction_limit': 0.1,        # 9. Automated reaction
            'aggressive_pattern_limit': 10,    # 10. Aggressive interaction
            'search_ratio_factor': 5,          # 11. Inconsistent user flow
            'community_report_limit': 5,       # 12. Community-based detection
            'coordinated_attack_limit': 20     # 13. Coordinated attack
        }

    # 1. High activity immediately after registration
    def check_high_activity_after_registration(self, actions_within_hour):
        return actions_within_hour > self.config['burst_actions_registration']

    # 2. IP Address duplication
    def check_ip_address_duplication(self, account_count):
        return account_count > self.config['ip_duplication_limit']

    # 3. Spam keyword detection
    def check_spam_keyword_detection(self, content):
        return any(word in content.lower() for word in self.config['spam_keywords'])

    # 4. Burst posting
    def check_burst_posting(self, posts_per_minute):
        return posts_per_minute > self.config['burst_post_limit']

    # 5. Abnormal Follower/Following ratio
    def check_abnormal_follow_ratio(self, followers, following):
        return followers == 0 and following > self.config['follow_limit']

    # 6. Comment spamming (Repetitive content)
    def check_comment_spamming(self, same_content_count):
        return same_content_count > self.config['comment_repeat_limit']

    # 7. High-speed commenting
    def check_high_speed_commenting(self, comments_per_minute):
        return comments_per_minute > self.config['burst_comment_limit']

    # 8. High-speed liking
    def check_high_speed_liking(self, likes_per_minute):
        return likes_per_minute > self.config['burst_like_limit']

    # 9. Automated reaction
    def check_automated_reaction(self, post_time, like_time):
        return (like_time - post_time).total_seconds() < self.config['auto_reaction_limit']

    # 10. Aggressive interaction pattern
    def check_aggressive_interaction(self, like_time, follow_time):
        return (follow_time - like_time).total_seconds() < self.config['aggressive_pattern_limit']

    # 11. Inconsistent user flow (Follow count vs SearchLog)
    def check_inconsistent_user_flow(self, follow_count, search_count):
        return follow_count > (search_count * self.config['search_ratio_factor'])

    # 12. Community-based detection
    def check_community_based_detection(self, distinct_reporters):
        return distinct_reporters >= self.config['community_report_limit']

    # 13. Coordinated attack/Paralysis attempt
    def check_coordinated_attack(self, report_count_within_10m):
        return report_count_within_10m > self.config['coordinated_attack_limit']

    def evaluate_user(self, user_metrics):
        score = 0
        reasons = []
        
        # 1: Detect high activity level right after the account is created
        if self.check_high_activity_after_registration(user_metrics.get('actions_within_hour', 0)):
            score += 30
            reasons.append("High activity immediately after registration")

        # 2: Identify multiple accounts sharing the same IP address
        if self.check_ip_address_duplication(user_metrics.get('ip_count', 0)):
            score += 30
            reasons.append("IP Address duplication detected")

        # 3: Filter content for specific blacklisted spam keywords
        if self.check_spam_keyword_detection(user_metrics.get('content', '')):
            score += 15
            reasons.append("Spam keywords detected in content")

        #  4: Monitor for abnormally high posting frequency per minute
        if self.check_burst_posting(user_metrics.get('posts_per_minute', 0)):
            score += 40
            reasons.append("Burst posting activity")

        # 5: Flag accounts with zero followers but excessive following counts
        if self.check_abnormal_follow_ratio(user_metrics.get('followers', 0), user_metrics.get('following', 0)):
            score += 35
            reasons.append("Abnormal Follower/Following ratio")

        # 6: Identify repetitive comment patterns (identical content)
        if self.check_comment_spamming(user_metrics.get('same_content_count', 0)):
            score += 20
            reasons.append("Repetitive comment content detected")

        # 7: Detect high-frequency commenting behavior
        if self.check_high_speed_commenting(user_metrics.get('comments_per_minute', 0)):
            score += 40
            reasons.append("High-speed commenting detected")

        # 8: Detect machine-like high-speed liking activity
        if self.check_high_speed_liking(user_metrics.get('likes_per_minute', 0)):
            score += 40
            reasons.append("High-speed liking detected")

        # 9: Check for non-human reaction time (sub-0.1 seconds)
        p_time, l_time = user_metrics.get('post_time'), user_metrics.get('like_time')
        if p_time and l_time and self.check_automated_reaction(p_time, l_time):
            score += 50
            reasons.append("Automated reaction (Instant response)")

        # 10: Identify aggressive interaction sequences (Like then immediate Follow)
        l_time_seq, f_time_seq = user_metrics.get('like_time'), user_metrics.get('follow_time')
        if l_time_seq and f_time_seq and self.check_aggressive_interaction(l_time_seq, f_time_seq):
            score += 25
            reasons.append("Aggressive interaction pattern")

        # 11: Detect mismatched user flow (High follow rate without search history)
        if self.check_inconsistent_user_flow(user_metrics.get('following', 0), user_metrics.get('search_count', 0)):
            score += 25
            reasons.append("Inconsistent user flow (Follow without search)")

        # 12: Weighted scoring based on distinct community reports
        if self.check_community_based_detection(user_metrics.get('reports', 0)):
            score += 60
            reasons.append("Multiple community reports received")

        # 13: Detect sudden spikes in reports suggesting a coordinated attack
        if self.check_coordinated_attack(user_metrics.get('reports_10m', 0)):
            score += 60
            reasons.append("Coordinated attack pattern detected")

        # Final decision logic based on the cumulative risk score
        if score >= 70:
            status = "Blocked"
        elif score >= 40:
            status = "Suspected"
        else:
            status = "Normal"

        return {
            "status": status,
            "score": score,
            "reasons": reasons
        }