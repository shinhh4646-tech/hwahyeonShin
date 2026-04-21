## LAB_08_MoreTrees

## 1. Team Members & Assigned Exercises

Exercise 1: Hwahyeon SHIN

Exercise 2: Jina Hwang

Exercise 3: Minkyeong KANG

## 2. Brief Description of Solutions

## Exercise 1
It implements a Binary Search Tree to efficiently manage user profiles and recommend friends. Using user_id as the key, it handles basic operations like insertion, search, and deletion. The core suggest_friends algorithm works by finding indirect connections , counting how often they appear, and returning the top recommendations based on frequency.


## Exercise 2



## Exercise 3



## 3. Complexity Analysis Questions

## Exercise 1
The BST's performance relies entirely on its balance. With random insertions, search operations maintain an efficient O(log n) average time complexity. However, if user IDs are inserted in sequential order, the tree degrades into a right-skewed linear structure which is same with linked tree, resulting in a worst-case O(n) search time. This severe imbalance drastically degrades the efficiency of the friend recommendation algorithm.
## Exercise 2

## Exercise 3




