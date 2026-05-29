import os
import django
from django.utils import timezone
from datetime import timedelta

# 1. Load Django Environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from app.models import Users, Post, Comment, Likes, SearchLog, Follow

def run_seed():
    print("🧹 Clearing up existing database records...")
    Follow.objects.all().delete()
    Likes.objects.all().delete()
    Comment.objects.all().delete()
    Post.objects.all().delete()
    Users.objects.all().delete()

    print("🌱 [Rules 1~11 All Algorithms] Starting bot detection simulation data seeding...")

    # Base normal user and post for rules context
    target_user = Users.objects.create(username="clean_user", password="123", status="Normal")
    target_post = Post.objects.create(user=target_user, content="This is a normal user post.")

    # ====================================================
    # [Rule 1] High Activity Right After Registration (> 50 posts within 1hr)
    # ====================================================
    print("-> Seeding Rule 1 (Early High Activity Bot)...")
    bot_1 = Users.objects.create(username="bot_rule_1", password="bot", created_at=timezone.now())
    for i in range(55): 
        Post.objects.create(user=bot_1, content=f"Spamming right after registration {i}")

    # ====================================================
    # [Rule 2] IP Address Duplication (> 5 accounts per IP)
    # ====================================================
    print("-> Seeding Rule 2 (IP Address Duplication Bots)...")
    duplicate_ip = "111.111.111.111"
    for i in range(6): 
        Users.objects.create(username=f"bot_rule_2_{i}", password="bot", last_login_ip=duplicate_ip)

    # ====================================================
    # [Rule 3] Spam Keyword Filtering ('gambling', 'ads', 'link')
    # ====================================================
    print("-> Seeding Rule 3 (Spam Keyword Bot)...")
    bot_3 = Users.objects.create(username="bot_rule_3", password="bot")
    Post.objects.create(user=bot_3, content="Earn easy money now! Click this online gambling link")

    # ====================================================
    # [Rule 4] Burst Posting Spike (> 100 posts within 1 min) - 3 Users 
    # ====================================================
    print("-> Seeding Rule 4 (Burst Posting Bots - 3 Users)...")
    for j in range(3): 
        bot_4 = Users.objects.create(username=f"bot_rule_4_{j}", password="bot")
        for i in range(105): 
            Post.objects.create(user=bot_4, content=f"Macro fast posting simulator {j}-{i}")

    # ====================================================
    #  [Rule 5] Abnormal Follow Ratio (0 followers & > 1000 followings)
    # ====================================================
    print("-> Seeding Rule 5 (Abnormal Follow Ratio Graph Bot)...")
    bot_5 = Users.objects.create(username="bot_rule_5", password="bot")
    for i in range(1005): 
        Follow.objects.create(follower=bot_5, following=target_user)

    # ====================================================
    #  [Rule 6] Comment Content Spam (> 10 identical comments)
    # ====================================================
    print("-> Seeding Rule 6 (Comment Content Spam Bot)...")
    bot_6 = Users.objects.create(username="bot_rule_6", password="bot")
    for i in range(15): 
        Comment.objects.create(post=target_post, user=bot_6, content="Buy this stock now! Mega returns guaranteed!")

    # ====================================================
    #  [Rule 7] Burst Commenting (> 100 comments within 1 min)
    # ====================================================
    print("-> Seeding Rule 7 (Burst Commenting Bot)...")
    bot_7 = Users.objects.create(username="bot_rule_7", password="bot")
    for i in range(105): 
        Comment.objects.create(post=target_post, user=bot_7, content=f"High-speed comment {i}")

    # ====================================================
    #  [Rule 8] Burst Liking (> 100 likes within 1 min)
    # ====================================================
    print("-> Seeding Rule 8 (Burst Liking Bot)...")
    bot_8 = Users.objects.create(username="bot_rule_8", password="bot")
    for i in range(105): 
        Likes.objects.create(user=bot_8, post=target_post)

    # ====================================================
    #  [Rule 9] Automated Fast Reactions (< 0.1s macro delay)
    # ====================================================
    print("-> Seeding Rule 9 (0.1s Fast Reaction Macro Bot)...")
    bot_9 = Users.objects.create(username="bot_rule_9", password="bot")
    fast_post = Post.objects.create(user=target_user, content="Macro target post")
    fast_post.created_at = timezone.now() - timedelta(seconds=1)
    fast_post.save()
    
    like_action = Likes.objects.create(user=bot_9, post=fast_post)
    like_action.created_at = fast_post.created_at + timedelta(seconds=0.05) 
    like_action.save()

    # ====================================================
    #  [Rule 11] Inconsistent Flow (Followings > Search Logs * 5)
    # ====================================================
    print("-> Seeding Rule 11 (Inconsistent Traffic Flow Bot)...")
    bot_11 = Users.objects.create(username="bot_rule_11", password="bot")
    for i in range(10): 
        Follow.objects.create(follower=bot_11, following=target_user)

    print("\n" + "="*50)
    print(" [Database Seed Complete] Mock bots are fully generated for all rules!")
    print("="*50)

if __name__ == "__main__":
    run_seed()