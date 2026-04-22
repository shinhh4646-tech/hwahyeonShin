## LAB_08_MoreTrees

## 1. Team Members & Assigned Exercises

Exercise 1: Hwahyeon SHIN

Exercise 2: Jina HWANG

Exercise 3: Minkyeong KANG

## 2. Brief Description of Solutions

## Exercise 1
It implements a Binary Search Tree to efficiently manage user profiles and recommend friends. Using user_id as the key, it handles basic operations like insertion, search, and deletion. The core suggest_friends algorithm works by finding indirect connections , counting how often they appear, and returning the top recommendations based on frequency.


## Exercise 2

The system is designed to efficiently manage a real-time "Trending Feed" using a Max-Heap to ensure the most popular posts are always accessible.

Structure (TrendingHeap): Combines a list-based Max-Heap with an Entry Map (Hash Map). This hybrid approach allows for logarithmic time complexity while maintaining the ability to locate any post instantly.

Core Operations:

Push: Inserts a new post at the end of the heap and uses _bubble_up to maintain the heap property. (O(logn))

Pop Max: Removes the root (highest likes) by swapping it with the last element and performing _bubble_down. (O(logn))

Update Likes: Utilizes the Map to jump directly to a post's index, updates the value, and restores order using either bubble-up or bubble-down. (O(logn))

Top-K Retrieval: Creates a temporary copy of the heap and extracts the top k elements sequentially.



## Exercise 3
This exercise focuses on two main features: a user search system and an activity analysis tool.

* **User Autocomplete (Trie):** A Trie structure was used to store and search usernames. It stores each character as a node, making it very fast to find users by their prefixes. It includes functions to insert new users, search for a specific user ID, and provide a list of autocomplete suggestions in alphabetical order. We also added functions to calculate the tree's height and total number of nodes to monitor the structure.

* **Activity Analysis (Segment Tree):** A Segment Tree was implemented to manage and analyze daily post data. By organizing data into a tree, it can quickly calculate the total sum, maximum, and minimum number of posts within any given date range. This is much more efficient than a simple list when dealing with frequent data lookups for specific periods, as it uses a divide-and-conquer approach to pre-calculate values.


## 3. Complexity Analysis Questions

## Exercise 1
The BST's performance relies entirely on its balance. With random insertions, search operations maintain an efficient O(log n) average time complexity. However, if user IDs are inserted in sequential order, the tree degrades into a right-skewed linear structure which is same with linked tree, resulting in a worst-case O(n) search time. This severe imbalance drastically degrades the efficiency of the friend recommendation algorithm.
## Exercise 2


1. Time Complexity of get_top_k(k) and Advantage over Sorting

Complexity: O(klogn).

Advantage: It is significantly faster than sorting the entire list, which takes O(nlogn). Since k (the number of trending posts) is usually much smaller than n (total posts), extracting only what is needed is more computationally efficient.

2. Cost of update_likes() using a Sorted Array

Complexity: O(n).

Reason: While finding a post in a sorted array might be fast, updating its value requires shifting all subsequent elements to maintain the sorted order, resulting in linear time complexity.

3. Modifying for 24-Hour Expiration

Lazy Deletion: Expired posts are only removed when they reach the root of the heap during a pop_max operation.

Secondary Min-Heap: A separate Min-Heap ordered by timestamp can be maintained to track and remove all posts that have exceeded the 24-hour limit before any major operation occurs.

## Exercise 3
1. **Time Complexity of query(l, r):** The query operation takes **$O(\log n)$**. Since the segment tree is a balanced tree with a height of $\lceil \log_2 n \rceil$, it only needs to visit a constant number of nodes (at most four) at each level to find the result, regardless of how large the range $(l, r)$ is.

2. **Space Complexity:** The segment tree uses **$O(n)$** space. For 365 days of data, it creates about $4n$ nodes (roughly 1,460 nodes). This means the memory needed grows linearly and stays at a manageable constant rate relative to the number of days.

3. **Update Cost & Comparison:** If we used a **Prefix Sum Array**, updating a single day's data would take $O(n)$ time because all subsequent cumulative sums would need to be recalculated. The **Segment Tree** is better for active and changing data because it can handle both updates and queries in **$O(\log n)$** time, providing a much better balance between data maintenance and retrieval speed.



