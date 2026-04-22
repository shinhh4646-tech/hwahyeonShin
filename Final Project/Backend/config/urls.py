"""
[Handover: 프로젝트 메인 URL 설정]
이 파일은 프로젝트 전체의 URL 라우팅을 결정하는 메인 게이트웨이입니다.
- 'app' 폴더의 urls.py를 포함(include)하여 메인 주소로 연결합니다.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1. Django 관리자 페이지 (기본 제공)
    path('admin/', admin.site.urls),
    
    # 2. 'app'의 URL 설정을 메인 경로('')로 가져오기
    # 이를 통해 사용자가 사이트에 접속하자마자 민경님이 만든 봇 감지 대시보드가 나타납니다.
    path('', include('app.urls')),
]