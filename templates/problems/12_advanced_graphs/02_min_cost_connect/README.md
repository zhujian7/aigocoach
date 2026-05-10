# Min Cost to Connect All Points

- **Difficulty**: Medium
- **Category**: Advanced Graphs
- **Topics**: minimum spanning tree, Prim's algorithm, heap
- **Link**: [NeetCode](https://neetcode.io/problems/min-cost-to-connect-points) | [LeetCode 1584](https://leetcode.com/problems/min-cost-to-connect-all-points/)

## Description

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the Manhattan distance between them: `|xi - xj| + |yi - yj|`.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

## Examples

**Example 1:**

![Example 1](assets/d.png)

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
```

**Example 2:**

![Example 2](assets/c.png)

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

**Example 3:**

```
Input: points = [[0,0],[1,1]]
Output: 2
Explanation: The Manhattan distance between the two points is |0-1| + |0-1| = 2.
```

## Constraints

- `1 <= points.length <= 1000`
- `-10^6 <= xi, yi <= 10^6`
- All pairs `(xi, yi)` are distinct.

## Function Signature

**Go:**

```go
func minCostConnectPoints(points [][]int) int
```

**Python:**
```python
def min_cost_connect_points(points: List[List[int]]) -> int:
```
