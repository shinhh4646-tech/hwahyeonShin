## LAB_10 : Backtracking, Optimization, DP & Greedy Algorithms

## 1. Team Members & Assigned Exercises

Exercise 1: Jina Hwang

Exercise 2: Hwahyeon Shin

Exercise 3: 

## 2. Brief Description of Solutions

## Exercise 1

Validation (is_valid_invitation): Checks every pair of people in the invited list to ensure no two individuals have a conflict (no edges exist between them).

Exact Search (find_max_invitations_exact): Uses a backtracking algorithm with pruning to explore all possible include/exclude combinations. It guarantees finding the absolute maximum independent set but is computationally heavy.

Greedy Approach (find_max_invitations_greedy): Heuristically builds the guest list by repeatedly selecting the person with the fewest conflicts (minimum degree) and removing them along with their conflicting neighbors. It is fast and scalable but does not guarantee the global maximum.

## Exercise 2
It s a viral marketing campaign as a 0/1 Knapsack problem, where the goal is to maximize the total reach of a promotional message without exceeding a fixed budget. The solution consists of three parts: a validation function to check if a selected group of users stays within the budget constraint, an exact dynamic programming approach that systematically guarantees the maximum possible reach, and a fast greedy heuristic that approximates the solution by prioritizing users with the highest reach-to-cost ratio.
## Exercise 3



## 3. Complexity Analysis Questions

## Exercise 1

1. Verification vs construction
Ease of Verification: Checking a provided list is computationally "easy" because it runs in polynomial time (O(k^2)).
Difficulty of Construction: Finding the optimal Maximum Independent Set is mathematically "hard" (NP-hard). To guarantee optimality, an algorithm must navigate a massive search space of all possible subsets (2^N).
Example (Cycle Graph C5 with 5 nodes): Verifying if the set {0,2} is valid takes virtually no time. Conversely, finding the actual maximum set from scratch requires an algorithm to backtrack and test numerous dead ends to definitively prove it found the best solution.

2. Growth of runtime
Exponential Growth: The total number of subsets grows exponentially at a rate of 2^N
The limit of N=100: Even with highly effective pruning, solving for N=100 via brute force is impossible because 2^100 represents an astronomically large search space that computers cannot process in a reasonable timeframe.
Large-Scale Data Processing: The greedy algorithm is highly scalable. Because it operates in polynomial time (e.g., O(∣V∣log∣V∣+∣E∣)), it can efficiently process massive graphs with N=1,000,000 in just seconds or minutes.

3. Optimality guarantee
Limitations of Greedy: The greedy approach only guarantees finding a locally optimal solution (a maximal set), but it frequently misses the absolute largest global set.
Real-World Alternatives (Big Tech & Social Networks):
Distributed Computing: Companies leverage massive parallel processing frameworks like Apache Spark GraphX to distribute graph calculations across thousands of servers simultaneously.
Graph Partitioning (Clustering): Massive networks are not processed whole. Algorithms like the Louvain method are used to partition the graph into smaller, disconnected "communities." Independent sets are found within these smaller clusters and then merged.

## Exercise 2
Its the fundamental trade-off between exact optimization and scalability. While Dynamic Programming guarantees the absolute maximum reach with a pseudo-polynomial time complexity of O(N*budget) by storing subproblems, it suffers from memory and computation explosion and becomes impossible for massive datasets  or continuous real-number costs. Consequently, real-world platforms must abandon exact methods and rely on the ratio-based Greedy algorithm; despite its vulnerability to suboptimal edge cases and poor worst-case approximation factors, it scales highly efficiently to process millions of users in real-time.

## Exercise 3


