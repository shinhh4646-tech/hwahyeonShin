"""
[Handover: 데이터베이스 모델 정의]
민경님이 작성한 schema.sql 및 ERD 구조를 Django ORM 모델로 구현하였습니다.
- 7개의 주요 테이블(Users, Post, Comment, Follow, Likes, SearchLog, Report)을 포함합니다.
- 각 필드명과 관계(ForeignKey)는 SQL 스키마와 동일하게 설정되었습니다.
"""
from django.db import models

class Users(models.Model):
    # 1. User Table: Information for all accounts
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='Normal') # Normal, Suspected, Blocked
    created_at = models.DateTimeField(auto_now_add=True)
    last_login_ip = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = 'Users'

class Post(models.Model):
    # 2. Post Table: User-generated posts
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='user_id')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Post'

class Comment(models.Model):
    # 3. Comment Table: Feedback on posts
    id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='post_id')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='user_id')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Comment'

class Follow(models.Model):
    # 4. Follow Table: User-to-user relationships
    id = models.BigAutoField(primary_key=True)
    follower = models.ForeignKey(Users, related_name='following_set', on_delete=models.CASCADE, db_column='follower_id')
    following = models.ForeignKey(Users, related_name='follower_set', on_delete=models.CASCADE, db_column='following_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Follow'

class Likes(models.Model):
    # 5. Like Table: Reaction to posts
    id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='post_id')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='user_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Likes'

class SearchLog(models.Model):
    # 6. SearchLog Table: User search history
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='user_id')
    keyword = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'SearchLog'

class Report(models.Model):
    # 7. Report Table: User reports for bot detection
    id = models.BigAutoField(primary_key=True)
    reporter = models.ForeignKey(Users, related_name='reports_made', on_delete=models.CASCADE, db_column='reporter_id')
    target = models.ForeignKey(Users, related_name='reports_received', on_delete=models.CASCADE, db_column='target_id')
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Report'