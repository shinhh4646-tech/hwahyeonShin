import datetime

class Post:
    def __init__(self, post_id, user_id, content, timestamp, likes, comments, shares):
        self.post_id = post_id 
        self.user_id = user_id 
        self.content = content 
        self.timestamp = timestamp 
        self.likes = likes 
        self.comments = comments 
        self.shares = shares 
        self.engagement_score = self.calculate_score(likes, comments, shares)
        self.next = None

    def calculate_score(self, likes, comments, shares):
        return (likes * 1) + (comments * 2) + (shares * 3)
    
    
    def __str__(self):
        return f"[Post{self.post_id}: score {self.engagement_score}]"


class PriorityQueue:
    def __init__(self):
        self.head = None
        self._size = 0

    def is_empty(self):
        return self.head is None 

    def size(self):
        return self._size 

    def enqueue(self, post):
        self._size += 1
        
        if self.head is None or self.head.engagement_score < post.engagement_score:
            post.next = self.head
            self.head = post
            return

        current = self.head
        while current.next is not None and current.next.engagement_score >= post.engagement_score:
            current = current.next

        post.next = current.next
        current.next = post

    def dequeue_max(self):
        if self.is_empty():
            return None
        max_post = self.head
        self.head = self.head.next
        return max_post

   
    def peek_max(self):
        return self.head

   
    def update_score(self, post_id, new_likes, new_comments, new_shares):
        current = self.head
        prev = None
        target_post = None

        
        while current is not None:
            if current.post_id == post_id:
                target_post = current
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                self._size -= 1
                break
            prev = current
            current = current.next

        
        if target_post is not None:
            target_post.likes = new_likes
            target_post.comments = new_comments
            target_post.shares = new_shares
            target_post.engagement_score = target_post.calculate_score(new_likes, new_comments, new_shares)
            target_post.next = None
            self.enqueue(target_post)

   
    def refresh_all(self):
        old_head = self.head
        self.head = None
        self._size = 0
        
        current = old_head
        while current is not None:
            next_node = current.next
            current.next = None
            self.enqueue(current)
            current = next_node

    def get_top_k(self, k):
        result = []
        current = self.head
        count = 0
        while current is not None and count < k:
            result.append(current)
            current = current.next
            count += 1
        return result

    def decay_older_than(self, target_timestamp):
        current = self.head
        while current is not None:
            if current.timestamp < target_timestamp:
                
                current.engagement_score = int(current.engagement_score * 0.8)
            current = current.next
        self.refresh_all()

