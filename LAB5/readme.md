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
