-- 1. Impossible Travel Detection (Spatiotemporal Anomaly)
-- Detects users who post from different locations at a speed exceeding 1,000 km/h
SELECT p1.user_id
FROM Post p1
JOIN Post p2 ON p1.user_id = p2.user_id
WHERE p1.id > p2.id 
AND p1.captured_at - p2.at < INTERVAL '1 hour'
AND (ST_DistanceSphere(ST_MakePoint(p1.longitude, p1.latitude), ST_MakePoint(p2.longitude, p2.latitude)) / 1000) > 1000;

-- 2. Real-time Verification Anomaly (Latency Detection)
-- Flags posts where the gap between capture time and server upload time is physically impossible or suspicious
SELECT user_id
FROM Post
WHERE created_at - captured_at < INTERVAL '0.1 second' 
OR created_at - captured_at > INTERVAL '10 minute';

-- 3. Behavioral Entropy Analysis (Mechanical Repetition)
-- Identifies accounts that post at the exact same hour and minute consistently, indicating automated scheduling
SELECT user_id
FROM Post
GROUP BY user_id, EXTRACT(HOUR FROM captured_at), EXTRACT(MINUTE FROM captured_at)
HAVING COUNT(*) > 7;

-- 4. High Activity Immediately After Registration
SELECT id FROM Users 
WHERE created_at > NOW() - INTERVAL '1 hour' 
AND id IN (SELECT user_id FROM Post GROUP BY user_id HAVING COUNT(*) > 50);

-- 5. IP Address Duplication (Multi-accounting)
SELECT last_login_ip, COUNT(*) FROM Users 
GROUP BY last_login_ip HAVING COUNT(*) > 5;

-- 6. Spam Keyword Filtering
SELECT user_id FROM Post 
WHERE content ILIKE '%Gambling%' OR content ILIKE '%Ads%' OR content ILIKE '%Link%';

-- 7. High-speed Liking (Speed Liking)
SELECT user_id FROM Likes 
WHERE created_at > NOW() - INTERVAL '1 minute' 
GROUP BY user_id HAVING COUNT(*) > 100;

-- 8. Automated Reaction (Instant Engagement)
SELECT l.user_id FROM Likes l 
JOIN Post p ON l.post_id = p.id 
WHERE l.created_at - p.created_at < INTERVAL '0.5 second';

-- 9. Abnormal Follower/Following Ratio
SELECT u.id FROM Users u
JOIN Follow f ON u.id = f.follower_id
GROUP BY u.id HAVING COUNT(f.following_id) > 1000 
AND (SELECT COUNT(*) FROM Follow WHERE following_id = u.id) = 0;

-- 10. Comment Spamming and Suspicious Links
SELECT user_id FROM Comment 
WHERE content LIKE '%http%' OR content LIKE '%★★★%'
GROUP BY user_id, content HAVING COUNT(*) > 5;

-- 11. Community-based Detection (Crowdsourced Reports)
SELECT target_id FROM Report 
GROUP BY target_id HAVING COUNT(DISTINCT reporter_id) >= 5;

-- 12. Inconsistent User Inflow (Follows without Search History)
SELECT f.follower_id FROM Follow f
GROUP BY f.follower_id 
HAVING COUNT(*) > (SELECT COUNT(*) FROM SearchLog s WHERE s.user_id = f.follower_id) * 10;
