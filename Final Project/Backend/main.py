"""
[Handover: 엔진 독립 테스트 스크립트]
이 파일은 웹 서버 실행 없이 core/engine.py의 로직을 독립적으로 검증합니다.
- SQL에 정의된 13가지 시나리오 중 주요 케이스를 시뮬레이션하여 결과를 출력합니다.
"""
from core.engine import ASnapEngine
from datetime import datetime, timedelta

def run_engine_test():
    engine = ASnapEngine()
    print("=== ASnap Bot Detection Engine: Logic Validation ===")

    # Test Case 1: IP Address duplication (Scenario 2)
    print("\n[Test 1] Scenario: IP Address duplication")
    ip_test = engine.check_ip_address_duplication(account_count=8)
    print(f"Result: {'DETECTED' if ip_test else 'Clean'} (Input: 8 accounts)")

    # Test Case 2: Abnormal Follower/Following ratio (Scenario 5)
    print("\n[Test 2] Scenario: Abnormal Follower/Following ratio")
    follow_test = engine.check_abnormal_follow_ratio(followers=0, following=1200)
    print(f"Result: {'DETECTED' if follow_test else 'Clean'} (Input: 0 Followers / 1200 Following)")

    # Test Case 3: Automated reaction (Scenario 9)
    print("\n[Test 3] Scenario: Automated reaction (Speed Check)")
    post_time = datetime.now()
    like_time = post_time + timedelta(seconds=0.05) # 0.05s difference
    auto_test = engine.check_automated_reaction(post_time, like_time)
    print(f"Result: {'DETECTED' if auto_test else 'Clean'} (Input: 0.05s response)")

    # Test Case 4: Comprehensive Evaluation (evaluate_user)
    print("\n[Test 4] Comprehensive User Evaluation")
    sample_metrics = {
        'ip_count': 10,
        'reports': 6,
        'posts_per_minute': 120
    }
    final_analysis = engine.evaluate_user(sample_metrics)
    print(f"Final Status: {final_analysis['status']}")
    print(f"Reasons: {', '.join(final_analysis['reasons'])}")

if __name__ == "__main__":
    run_engine_test()