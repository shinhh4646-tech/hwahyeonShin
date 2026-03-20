# LAB_04: Recursive Algorithms

## 1. Team Members & Assigned Exercises
Exercise 1: Jina Hwang - Recursive Comment Thread Traversal  
Exercise 2: Minkyeong Kang - Recursive Content Aggregation (Divide & Conquer)  
Exercise 3: Hwahyeon Shin - Converting Recursion to Iteration

## 2. Brief Description of Solutions

Exercise 1 (Recursive Traversal): 
Implemented a CommentNode structure to represent nested social media comment threads.
Developed recursive functions for depth-first traversal to count total comments, sum up likes, and calculate the maximum nesting depth.
Added recursive search by user/keyword and a cascade deletion feature that removes a target comment along with all its replies.

Exercise 2 (Divide & Conquer): 
Applied Divide and Conquer to find the maximum, sum, and average engagement scores by recursively splitting the post array.
Implemented Merge Sort (O(n log n)) to rank posts by engagement.
Used binary search-style recursion to identify the peak hour of likes in O(log n) time.

Exercise 3 (Iteration with Explicit Stack): 
Converted recursive thread flattening into an iterative version using an explicit stack in heap memory to ensure stability for deep threads.
Used a State Machine approach with START and DONE labels to manually track traversal progress without the system call stack.
Implemented tail recursion and loop conversion for comment counting to optimize memory usage.

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
