"""
[Handover: 백엔드-프론트엔드 연결 뷰]
이 파일은 데이터베이스(models.py)와 감지 엔진(engine.py)을 연결합니다.
- 사용자의 활동 데이터를 수집하여 13가지 봇 감지 로직에 투입합니다.
- 최종 분석 결과(status, score 등)를 'index.html' 템플릿으로 전달합니다.
"""
from django.shortcuts import render
from .models import Users, Post, Report, Likes, Comment
from core.engine import ASnapEngine
from django.utils import timezone
from datetime import timedelta

def index(request):
    engine = ASnapEngine()
    
    # 예시: 특정 유저의 봇 의심 증거 수집 (Scenarios 12, 4, 8 등)
    # 실제 운영 시에는 request.user 또는 파라미터로 받은 유저를 분석합니다.
    test_user = Users.objects.first()
    
    if test_user:
        # Scenario 12: Community-based detection (Distinct reports)
        distinct_reports = Report.objects.filter(target=test_user).values('reporter_id').distinct().count()
        
        # Scenario 4 & 8: Burst activities within 1 minute
        one_minute_ago = timezone.now() - timedelta(minutes=1)
        posts_last_min = Post.objects.filter(user=test_user, created_at__gte=one_minute_ago).count()
        likes_last_min = Likes.objects.filter(user=test_user, created_at__gte=one_minute_ago).count()
        
        # 엔진에 수집된 데이터 전달
        user_metrics = {
            'reports': distinct_reports,
            'posts_per_minute': posts_last_min,
            'likes_per_minute': likes_last_min,
            'ip_count': 1 # 예시값 (실제는 DB 집계 결과 전달)
        }
        
        analysis_result = engine.evaluate_user(user_metrics)
    else:
        analysis_result = {"status": "No Data", "score": 0, "reasons": []}

    context = {
        'analysis': analysis_result,
        'user': test_user,
        'project_name': 'ASnap: Bot Detection System'
    }
    
    # Frontend 폴더 내의 index.html 호출
    return render(request, 'index.html', context)