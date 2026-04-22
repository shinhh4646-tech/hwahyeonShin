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
        """[Handover] 위 13가지 로직을 종합하여 점수를 산출하고 최종 상태를 리턴합니다."""
        score = 0
        reasons = []
        
        # 실제 구현 시에는 유저의 데이터를 받아 각 check_ 함수를 돌려 score를 합산합니다.
        # 예시: IP 중복 시 점수 추가
        if self.check_ip_address_duplication(user_metrics.get('ip_count', 0)):
            score += 30
            reasons.append("IP Address duplication detected")
            
        status = "Blocked" if score >= 70 else "Normal"
        return {"status": status, "score": score, "reasons": reasons}