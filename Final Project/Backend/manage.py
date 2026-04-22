#!/usr/bin/env python
"""
[Handover: Django 리소스 관리자]
이 스크립트는 Django 프로젝트의 관리 작업을 수행하기 위한 커맨드라인 유틸리티입니다.
- 서버 실행(runserver), DB 마이그레이션(migrate) 등의 명령을 처리합니다.
"""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()