## LAB_05: Basics of Graph Structures

## 1. Team Members & Assigned Exercises

Exercise 1: Jina HWANG

Exercise 2: Minkyeong KANG

Exercise 3: Hwahyeon SHIN

## 2. Brief Description of Solutions

## Exercise 1
This project implements a SocialGraph class using two concurrent data structures to model social network dynamics:

Dual-Storage System: The class maintains an Adjacency Matrix (2D Array) for O(1) connectivity checks and an Adjacency List (Array of Lists) for memory-efficient storage.

Optimized Operations: Friendship updates (Add/Remove) are synchronized across both structures, ensuring data integrity while allowing for direct performance comparison.

Analytical Metrics: It calculates network Density and Completeness using global counters, and generates a Degree Distribution map to analyze user connectivity patterns.

Representation Fluidity: Built-in conversion functions (matrix_to_list, list_to_matrix) allow the graph to adapt its structure based on specific use cases or memory constraints.

Conclusion: The solution demonstrates that while matrices are faster for updates, the adjacency list is the only scalable choice for massive, sparse social networks.


## Exercise 2
This exercise focuses on deep exploration of social circles using **Depth-First Search (DFS)**:
* **Recursive Traversal**: Implemented a recursive DFS algorithm to explore social connections as deep as possible before backtracking.
* **Connectivity Mapping**: Used DFS to identify all reachable users from a starting point, helping to understand the boundaries of isolated social clusters.
* **Path Finding**: Leveraged the stack-based nature of DFS to discover complex, non-linear friendship chains within the network.


## Exercise 3
This exercise implements **Breadth-First Search (BFS)** to analyze distances and shortest paths in a social network:
* **Level-Order Exploration**: Developed a queue-based BFS to traverse the network layer-by-layer, ensuring that users are visited in order of their proximity to the starting point.
* **Distance Tracking**: Integrated a distance mapping system that calculates the exact "degrees of separation" between the source user and everyone else in the graph.
* **Path Reconstruction**: Implemented a "parent-tracking" mechanism to not only find the distance but reconstruct the specific chain of friends that forms the shortest path.
* **Social Analytics**: Built tools to calculate the average degrees of separation across the network and provide friend recommendations based on "friends-of-friends" frequency.

## 3. Complexity Analysis Questions

## Exercise 1

1. Adjacency Matrix offers superior O(1) speed for connectivity checks and updates, while Adjacency List performs at O(d).

2. For 1 billion users, the Matrix is practically impossible (4 Exabytes), whereas the List is highly efficient (604 GB).

3. Use Matrix for high-frequency updates in small graphs, and List for scalability in massive social networks.

## Exercise 2
1. **Time Complexity**: $O(V + E)$, as each user (Vertex) and friendship (Edge) is visited once during the recursive calls.
2. **Space Complexity**: $O(V)$ in the worst case (e.g., a long linear chain) due to the recursion stack and visited set.
3. **Application**: Best suited for tasks like finding cycles in a graph or exploring all possible paths in a deeply nested social structure.


## Exercise 3
1. **Time and Space Complexity**: Time $O(V + E)$ and Space $O(V)$. BFS uses a queue to explore wide, while DFS goes deep; both visit all nodes/edges once.
2. **Shortest Path Guarantee**: BFS is guaranteed to find the shortest path in unweighted networks because it explores all nodes at distance $d$ before moving to $d+1$.
3. **Six Degrees of Separation**: BFS is used because it explores neighbors layer-by-layer, making it efficient for finding connections within a small, specific number of steps.
4. **Shortest Friendship Chain**: BFS is the optimal choice as it always finds the minimum number of edges to connect two users. DFS may find a much longer path first.


