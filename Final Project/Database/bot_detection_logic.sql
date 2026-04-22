-- 1. High activity immediately after registration (Over 50 actions within 1 hour of joining)
-- 1. 가입 직후 비정상적으로 많은 활동 (가입 후 1시간 내 액션 50개 이상)
SELECT id FROM Users 
WHERE created_at > NOW() - INTERVAL '1 hour' 
AND id IN (SELECT user_id FROM Post GROUP BY user_id HAVING COUNT(*) > 50);

-- 2. IP Address duplication (Multiple accounts sharing the exact same IP)
-- 2. 여러 계정이 같은 IP 주소 사용
SELECT last_login_ip, COUNT(*) AS account_count FROM Users 
GROUP BY last_login_ip HAVING COUNT(*) > 5;

-- 3. Spam keyword detection (Content containing 'Gambling', 'Ads', or 'Link' - Case-insensitive)
-- 3. 게시물 본문에 스팸 키워드 포함 (e.g., Gambling, Ads, Link Click)
SELECT user_id FROM Post 
WHERE content ILIKE '%Gambling%' OR content ILIKE '%Ads%' OR content ILIKE '%Link%';

-- 4. Burst posting (Creating over 100 posts within a single minute)
-- 4. 동일 ID가 짧은 시간(1분)에 수백 개 Post 작성
SELECT user_id FROM Post 
WHERE created_at > NOW() - INTERVAL '1 minute' 
GROUP BY user_id HAVING COUNT(*) > 100;

-- 5. Abnormal Follower/Following ratio (0 Followers but over 1000 Following)
-- 5. 팔로워 수 0인데 팔로잉만 수천 명 (비정상적 비율)
SELECT u.id FROM Users u
JOIN Follow f ON u.id = f.follower_id
GROUP BY u.id HAVING COUNT(f.following_id) > 1000 
AND (SELECT COUNT(*) FROM Follow WHERE following_id = u.id) = 0;

-- 6. Comment spamming (Repetitive content, suspicious links, or excessive symbols)
-- 6. 댓글 도배 (동일 내용 반복 또는 특수문자 패턴)
SELECT user_id FROM Comment 
WHERE content LIKE '%http%' OR content LIKE '%★★★%'
GROUP BY user_id, content HAVING COUNT(*) > 10;

-- 7. High-speed commenting (Writing over 100 comments within 1 minute)
-- 7. 짧은 시간(1분) 내 과도한 댓글 작성
SELECT user_id FROM Comment 
WHERE created_at > NOW() - INTERVAL '1 minute' 
GROUP BY user_id HAVING COUNT(*) > 100;

-- 8. High-speed liking (Clicking over 100 likes within 1 minute)
-- 8. 짧은 시간(1분) 내 과도한 좋아요 클릭 (Likes 테이블 사용)
SELECT user_id FROM Likes 
WHERE created_at > NOW() - INTERVAL '1 minute' 
GROUP BY user_id HAVING COUNT(*) > 100;

-- 9. Automated reaction (Liking a post within 0.1 seconds of its creation)
-- 9. 자동 좋아요 감지 (Post 생성 후 0.1초 내 Likes 생성)
SELECT l.user_id FROM Likes l 
JOIN Post p ON l.post_id = p.id 
WHERE l.created_at - p.created_at < INTERVAL '0.1 second';

-- 10. Aggressive interaction pattern (Liking multiple posts and following the author immediately)
-- 10. 공격적 접근 패턴 (좋아요 여러 개 누른 직후 팔로우)
SELECT l.user_id FROM Likes l 
JOIN Follow f ON l.user_id = f.follower_id 
WHERE l.created_at < f.created_at AND f.created_at - l.created_at < INTERVAL '10 second';

-- 11. Inconsistent user flow (Extremely high Follow count compared to SearchLog history)
-- 11. 유입 경로 부정확 (SearchLog 흔적 대비 Follow 수 과다)
SELECT f.follower_id FROM Follow f
GROUP BY f.follower_id 
HAVING COUNT(*) > (SELECT COUNT(*) FROM SearchLog s WHERE s.user_id = f.follower_id) * 5;

-- 12. Community-based detection (User reported by 5 or more unique reporters)
-- 12. 다수 유저로부터 신고 접수 (서로 다른 5명 이상)
SELECT target_id FROM Report 
GROUP BY target_id HAVING COUNT(DISTINCT reporter_id) >= 5;

-- 13. Coordinated attack/Paralysis attempt (Massive reporting within 10 minutes of a post being created)
-- 13. 시스템 마비/집단 공격 의심 (게시물 작성 직후 대량 신고 발생)
SELECT r.target_id FROM Report r
JOIN Post p ON r.target_id = p.user_id
WHERE r.created_at - p.created_at < INTERVAL '10 minute'
GROUP BY r.target_id HAVING COUNT(*) > 20;