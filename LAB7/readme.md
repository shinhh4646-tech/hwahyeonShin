## LAB_07: More Recursive Algorithms and Structures

## 1. Team Members & Assigned Exercises

Exercise 1: Jina HWANG

Exercise 2: Hwahyeon SHIN

Exercise 3: Minkyeong KANG

## 2. Brief Description of Solutions

## Exercise 1

The proposed system implements a Divide and Conquer spatial analysis tool using a Quadtree structure to identify high-density regions.

Recursive Splitting (split_region): This procedure systematically decomposes a 2D space by bisecting the width and height into four equal quadrants until a minimum size is reached.

Density Assessment (count_points_in_region): A utility function that performs a linear search through all data points to calculate how many fall within specific rectangular boundaries.

Dense Region Identification (find_dense_regions): This core function merges splitting logic with density checks, filtering the space to only return areas where the point count exceeds a defined threshold.

Data Integrity: The implementation relies on strict comparison operators (≥ and <) to ensure no points are double-counted or missed at regional borders.

Result Aggregation: Found dense regions are collected into a list data structure, preserving their spatial coordinates and point counts for further analysis

## Exercise 2
The draw_sierpinski function generates a Sierpinski triangle by repeatedly subdividing an initial triangle into three smaller constituent triangles until the target depth is reached. Similarly, the draw_tree function simulates natural branching by drawing a line segment and recursively spawning two smaller segments at 30 angles. To evaluate these patterns, the fractal_dimension function implements the box-counting method by overlaying grids of decreasing sizes over the fractal, counting the intersecting boxes, and calculating the slope of the linear regression on a log(1/size)graph to determine the shape's fractal dimension


## Exercise 3
This solution implements terrain generation and error checking using recursive algorithms.
* **midpoint_displacement:** It generates a 1D line by splitting segments in half and adding a random height value to the midpoint at each step.
* **generate_terrain:** It creates a 2D grid using the Diamond-Square logic, where it calculates the average of neighboring points and adds a random offset to the center and edges.
* **detect_artifacts:** This function scans the final grid to find points where the height difference between neighbors is larger than a set threshold.


## 3. Complexity Analysis Questions

## Exercise 1
The complexity of this spatial splitting algorithm is primarily driven by the geometry of the space rather than the number of points.

Recursive Depth: For an S×S square area, the depth (D) of the recursive tree is log 2S, representing the number of times the side length is halved.

Total Operations: In a full decomposition, the total number of recursive calls follows a 4-ary tree geometric series:  

Computational Efficiency: The non-adaptive version is O(4 *D), meaning it splits every quadrant regardless of whether it contains data.

Clustering Performance: If points are clustered in one corner, the algorithm remains inefficient as it still performs a full decomposition on empty spaces.

Adaptive Optimization: To improve efficiency, "Adaptive Quadtrees" are recommended, which only initiate a split if the current region contains a minimum number of points.

## Exercise 2
The time complexity for generating these fractals is exponential due to the branching nature of the recursive calls.

## Exercise 3
1. For a line with depth 10, the total number of midpoints is $2^{10} - 1 = 1023$. This is because each recursive level splits every existing segment into two, following a geometric series.
2. If roughness is 0, the terrain becomes perfectly flat as no random displacement is added. If roughness is 2, the terrain becomes very jagged and irregular due to large height variations.


