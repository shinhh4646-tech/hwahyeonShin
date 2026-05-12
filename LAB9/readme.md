## LAB_09 : MoreHardProblems

## 1. Team Members & Assigned Exercises

Exercise 1: Hwahyeon SHIN

Exercise 2:

Exercise 3: 

## 2. Brief Description of Solutions

## Exercise 1
This exercise implements a solution for the minimum dominating set problem within a social network graph to identify the smallest group of influencers needed to cover all users. The implementation features three core functions: a verification algorithm to validate candidate sets in O(N+E) time, an exact brute-force search for small-scale graphs (N<20), and a greedy approximation that repeatedly selects the node with the highest coverage of remaining users.

## Exercise 2


## Exercise 3


## 3. Complexity Analysis Questions

## Exercise 1
The complexity analysis highlights the fundamental difference between verification, which is efficient at O(N+E), and construction, which is computationally expensive because finding the exact optimum requires checking 2^N potential subsets. While brute force is feasible for N=20, it becomes mathematically impossible for $N=100$ due to exponential growth. Consequently, real social networks rely on greedy heuristics that can scale to millions of nodes, even though they do not always guarantee an absolute minimum result

## Exercise 2


## Exercise 3

