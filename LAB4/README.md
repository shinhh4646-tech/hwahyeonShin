# LAB_04: Recursive Algorithms


## 1. Team Members & Assigned Exercises
Exercise 1: Jina Hwang - Recursive Comment Thread Traversal  
Exercise 2: Minkyeong Kang - Recursive Content Aggregation (Divide & Conquer)  
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

| Exercise | Time Complexity | Space Complexity | Reason |
| :--- | :--- | :--- | :--- |
| Comment Traversal | O(n) | O(d) | Every node is visited once; space depends on the nesting depth (d). |
| Max Engagement | O(n) | O(log n) | Entire array is checked; recursion depth is log n. |
| Merge Sort | O(n log n) | O(n) | Standard sorting complexity; requires extra space for merging. |
| Peak Hour Search | O(log n) | O(log n) | Binary search logic reduces search space by half each step. |
| Iterative Flatten | O(n) | O(d) | Visits n comments; manual stack size depends on depth (d). |


## 4. Complexity Analysis Questions

Recursion Depth & Limits: Recursion depth is determined by the maximum nesting level. Very deep threads (1000+) can cause StackOverflowError as they exceed the system's fixed call stack size.
Recursive vs. Iterative: Iterative implementations are safer for production systems because they use heap memory, which is significantly larger and more flexible than the call stack.
Tail Recursion: By making the recursive call the final action, the compiler can reuse stack frames, reducing space complexity from O(d) to O(1).
State Machine: Necessary for iterative processing of nested structures because loops do not "remember" the traversal state like recursion does.
