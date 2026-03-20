# LAB_04: Recursive Algorithms


## 1. Team Members & Assigned Exercises
Exercise 1: Jina Hwang - Recursive Comment Thread Traversal  
Exercise 2: Minkyeong Kang - Recursive Content Aggregation with divide & Conquer  
Exercise 3: Hwahyeon Shin - Converting Recursion to Iteration



## 2. Brief Description of Solutions

Exercise 1 (Recursive Comment Thread Traversal):  
Made a CommentNode structure to manage nested comments as a tree.  
Used recursion to display comments with indentation and count the total number of replies and likes.  
Added a search function for specific users and a delete function that also removes all sub-replies.  

Exercise 2 (Recursive Content Aggregation with Divide & Conquer):  
Used Divide and Conquer by splitting the post list in half to find the max engagement and average.  
Implemented Merge Sort to rank posts and used a recursive search to find the peak time for likes.  

Exercise 3 (Iteration with Explicit Stack):  
Changed recursive functions into loops using a manual stack to prevent the program from crashing on long threads.  
Used START and DONE labels to keep track of the progress in nested comments without the system stack.  
Applied tail recursion and while loops for counting comments to save memory.



## 3. Complexity Analysis Summary

| Exercise | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| Exercise 1: Recursive Traversal | O(n) | O(d) | Every comment node (n) must be visited once. Space depends on the max nesting depth (d).  |
| Exercise 2: Max Engagement | O(n) | O(log n) | Even with splitting, every post must be checked at least once. Recursion depth is log n.  |
| Exercise 2: Merge Sort | O(n log n) | O(n) | Standard complexity for dividing and merging. Needs extra space for the temporary list.  |
| Exercise 2: Peak Hour Search | O(log n) | O(log n) | Uses binary search logic to reduce the search range by half in each recursive step.  |
| Exercise 3: Iterative Flatten | O(n) | O(d) | Visits all n nodes like recursion. Manual stack size is determined by the max thread depth (d).  |



## 4. Complexity Analysis Questions

Recursion Depth & Limits: Recursion depth is determined by the maximum nesting level. Very deep threads (1000+) can cause StackOverflowError as they exceed the system's fixed call stack size.
Recursive vs. Iterative: Iterative implementations are safer for production systems because they use heap memory, which is significantly larger and more flexible than the call stack.
Tail Recursion: By making the recursive call the final action, the compiler can reuse stack frames, reducing space complexity from O(d) to O(1).
State Machine: Necessary for iterative processing of nested structures because loops do not "remember" the traversal state like recursion does.
