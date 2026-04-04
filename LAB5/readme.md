## LAB_05: Basics of Tree Structures

## 1. Team Members & Assigned Exercises

Exercise 1: Hwahyeon Shin

Exercise 2: Jina Hwang

Exercise 3: Minkyeong Kang

## 2. Brief Description of Solutions

## Exercise 1


## Exercise 2

Exercise 2 outlines the fundamental algorithms for traversing and analyzing a CategoryNode tree structure, specifically focusing on how different traversal methods serve distinct functional purposes.

First, In-order traversal visits nodes in a Left-Root-Right sequence, making it ideal for collecting sorted lists or maintaining a running total of metrics across the tree. Pre-order traversal (Root-Left-Right) is the most appropriate choice for exporting social network category structures, as it ensures a parent category is processed before its subcategories, preserving the natural hierarchy. Conversely, Post-order traversal (Left-Right-Root) is essential for metric aggregation, such as calculating total post counts, because it requires subcategory data to be fully processed before finalizing the parent’s value.

Beyond simple visits, these traversals enable analytical functions like finding the most popular category by recursively comparing post_count values across all nodes. In terms of efficiency, these methods operate at a time complexity of O(n), since every node must be visited once, and a space complexity of O(h), proportional to the height of the tree. Finally, while recursion is standard, these algorithms can be implemented iteratively using a Stack to handle deep trees more robustly, ensuring that even large-scale social data can be processed without memory overflows.

## Exercise 3

Exercise 3 focused on implementing a Generalized Tree (N-ary Tree) to represent social network categories and converting it into a Binary Tree representation for algorithmic efficiency.

The core of the solution lies in the "First Child, Next Sibling" transformation. In this model, each BinaryNode uses its left pointer to point to its first child and its right pointer to point to its immediate sibling. This allows a multi-child tree to be represented using only two pointers per node without losing any hierarchical information.

The implementation also included essential tree metrics. Fan-out was calculated by finding the maximum number of children any single node possesses, while the Branching Factor was derived by averaging the number of children across all non-leaf nodes. These metrics provide quantitative insights into the "width" and "density" of the category hierarchy. By reusing count_nodes and count_leaves functions, the branching factor was computed efficiently, demonstrating modular algorithm design.


## 3. Complexity Analysis Questions

## Exercise 1

## Exercise 2

1. Complexity Summary

Time: O(n) — All nodes are visited once.

Space: O(h) — Proportional to tree height (stack depth).

2. Metrics: Pre vs. Post-order

Post-order is best. It uses a bottom-up approach, calculating child values before the parent's total.

3. Iterative Stack (Pre-order)

Push Root.

Pop node, process it.

Push Right, then Push Left (so Left is processed first via LIFO).

4. Export: Why Pre-order?

Pre-order is best. It visits Parent → Child, keeping the hierarchy intuitive (like a Table of Contents) and making tree reconstruction easy.

## Exercise 3

**1. Binary vs. Generalized**
* **Generalized:** Intuitive hierarchy, fast child access. Complex memory management.
* **Binary:** Simple 2-pointer structure, easy implementation. Slow sibling access.

**2. Space Complexity**
* **$O(n)$ for both.** Space is proportional to the number of nodes $n$.

**3. Traversal Complexity**
* **$O(n)$ for both.** Every node must be visited once.

**4. Large Social Network**
* **Generalized.** Faster to access sub-categories directly from a list than traversing siblings.

**5. Logic & Time Complexity**
* **Logic:** Link first child to Left, then link siblings to Right.
* **Time:** **$O(n)$**. All nodes processed once during conversion.
