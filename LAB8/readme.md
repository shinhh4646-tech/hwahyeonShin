## LAB_08_MoreTrees

## 1. Team Members & Assigned Exercises

Exercise 1: Hwahyeon SHIN

Exercise 2: Jina HWANG

Exercise 3: Minkyeong KANG

## 2. Brief Description of Solutions

## Exercise 1
It implements a Binary Search Tree to efficiently manage user profiles and recommend friends. Using user_id as the key, it handles basic operations like insertion, search, and deletion. The core suggest_friends algorithm works by finding indirect connections , counting how often they appear, and returning the top recommendations based on frequency.


## Exercise 2



## Exercise 3
This exercise focuses on two main features: a user search system and an activity analysis tool.

* **User Autocomplete (Trie):** A Trie structure was used to store and search usernames. It stores each character as a node, making it very fast to find users by their prefixes. It includes functions to insert new users, search for a specific user ID, and provide a list of autocomplete suggestions in alphabetical order. We also added functions to calculate the tree's height and total number of nodes to monitor the structure.

* **Activity Analysis (Segment Tree):** A Segment Tree was implemented to manage and analyze daily post data. By organizing data into a tree, it can quickly calculate the total sum, maximum, and minimum number of posts within any given date range. This is much more efficient than a simple list when dealing with frequent data lookups for specific periods, as it uses a divide-and-conquer approach to pre-calculate values.


## 3. Complexity Analysis Questions

## Exercise 1
The BST's performance relies entirely on its balance. With random insertions, search operations maintain an efficient O(log n) average time complexity. However, if user IDs are inserted in sequential order, the tree degrades into a right-skewed linear structure which is same with linked tree, resulting in a worst-case O(n) search time. This severe imbalance drastically degrades the efficiency of the friend recommendation algorithm.
## Exercise 2

## Exercise 3
1. **Time Complexity of query(l, r):** The query operation takes **$O(\log n)$**. Since the segment tree is a balanced tree with a height of $\lceil \log_2 n \rceil$, it only needs to visit a constant number of nodes (at most four) at each level to find the result, regardless of how large the range $(l, r)$ is.

2. **Space Complexity:** The segment tree uses **$O(n)$** space. For 365 days of data, it creates about $4n$ nodes (roughly 1,460 nodes). This means the memory needed grows linearly and stays at a manageable constant rate relative to the number of days.

3. **Update Cost & Comparison:** If we used a **Prefix Sum Array**, updating a single day's data would take $O(n)$ time because all subsequent cumulative sums would need to be recalculated. The **Segment Tree** is better for active and changing data because it can handle both updates and queries in **$O(\log n)$** time, providing a much better balance between data maintenance and retrieval speed.



