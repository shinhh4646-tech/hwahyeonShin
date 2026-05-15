## LAB_09 : MoreHardProblems

## 1. Team Members & Assigned Exercises

Exercise 1: Hwahyeon SHIN

Exercise 2: Minkyeong KANG

Exercise 3: Jina Hwang

## 2. Brief Description of Solutions

## Exercise 1
This exercise implements a solution for the minimum dominating set problem within a social network graph to identify the smallest group of influencers needed to cover all users. The implementation features three core functions: a verification algorithm to validate candidate sets in O(N+E) time, an exact brute-force search for small-scale graphs (N<20), and a greedy approximation that repeatedly selects the node with the highest coverage of remaining users.

## Exercise 2
This exercise implements a solution for the conflict-free labeling problem, which is equivalent to the graph coloring problem. The goal is to assign integer labels to users so that connected users have different labels while minimizing the total number of distinct labels used. The implementation includes a validation function that checks whether a given labeling is valid, a backtracking function that attempts to color the graph using at most k labels, and a search function that finds the minimum number of labels by trying k = 1, 2, ..., N until a valid labeling is found.

## Exercise 3

This lab focuses on optimizing advertisement reach within a constrained budget, modeled as a variation of the 0/1 Knapsack Problem. Three primary functions were implemented:

maximize_reach (Exact Solution): Utilizes Dynamic Programming (DP) to find the absolute optimal set of users. By constructing a 2D lookup table (O(N×budget)), the algorithm evaluates every possible sub-budget to ensure the maximum total influence is achieved. It then uses backtracking to identify the specific users included in the optimal selection.

is_within_budget (Validation): A linear helper function (O(N)) that sums the costs of a given selection and compares it against the total budget to verify feasibility.

fast_alternative_strategy (Greedy Heuristic): Implements a Greedy approach by sorting users based on their influence-to-cost ratio. While significantly faster (O(NlogN)) than DP, it provides a heuristic solution that may not always reach the theoretical optimum but is highly efficient for large-scale data.


## 3. Complexity Analysis Questions

## Exercise 1
The complexity analysis highlights the fundamental difference between verification, which is efficient at O(N+E), and construction, which is computationally expensive because finding the exact optimum requires checking 2^N potential subsets. While brute force is feasible for N=20, it becomes mathematically impossible for $N=100$ due to exponential growth. Consequently, real social networks rely on greedy heuristics that can scale to millions of nodes, even though they do not always guarantee an absolute minimum result

## Exercise 2
For this problem, checking whether a given labeling is valid is easier than finding a valid labeling. Verification only requires checking each edge once, so its complexity is O(E). However, finding a labeling with k labels can be exponential because each of the N nodes may try up to k possible labels, giving a worst-case complexity of O(k^N). If k = 1 and the graph has at least one edge, the labeling fails immediately because connected nodes would receive the same label. A complete graph K_n needs n labels, while an empty graph needs only 1 label.

## Exercise 3

DP Efficiency: DP avoids exponential time complexity by using a lookup table to store results of overlapping subproblems, reducing the workload to O(N×budget).

Scalability Limits: For massive inputs (e.g., N=10,000, Budget=1,000,000), DP becomes infeasible due to high memory consumption (approx. 40GB RAM) and the sheer volume of operations (10 billion), which exceeds standard hardware capabilities.

Integer vs. Real Costs: DP relies on discrete integer steps to index the table. If costs are real numbers, the number of columns becomes infinite, making standard DP impossible to implement.

Greedy vs. Exact: The ratio-based greedy strategy can be arbitrarily worse (approximation factor near 0) because a small, high-ratio item can "block" a much larger, more valuable item from being selected.

Practical Application: In real-world platforms like Pulse, heuristics are preferred over exact DP because they are faster, support real-time processing, scale easily to millions of users, and handle decimal-based costs naturally.

