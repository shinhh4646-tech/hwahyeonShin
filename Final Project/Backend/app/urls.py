"""
[Handover: 앱 단위 URL 설정]
이 파일은 'app' 내의 뷰 기능을 특정 URL 경로와 연결합니다.
- 메인 페이지 접속 시 views.py의 index 함수가 호출되도록 설정되었습니다.
"""
from django.urls import path
from . import views

urlpatterns = [
    # 메인 페이지 경로 ('') 접속 시 index 뷰 실행
    path('', views.index, name='index'),
]