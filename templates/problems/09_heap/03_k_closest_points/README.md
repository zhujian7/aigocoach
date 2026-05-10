# K Closest Points to Origin

- **Difficulty**: Medium
- **Category**: Heap
- **Topics**: max-heap, priority queue, geometry
- **Link**: [NeetCode](https://neetcode.io/problems/k-closest-points-to-origin) | [LeetCode 973](https://leetcode.com/problems/k-closest-points-to-origin/)

## Description

![k-closest-points-to-origin](assets/closestplane1.jpg)

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`. The distance between two points on the X-Y plane is the Euclidean distance: `sqrt(xi^2 + yi^2)`. You may return the answer in any order, and the answer is guaranteed to be unique (except for the order in which it is returned).

## Examples

**Example 1:**

```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation: Distance of (1,3) from origin = sqrt(10). Distance of (-2,2) from origin = sqrt(8). Since sqrt(8) < sqrt(10), (-2,2) is the closest.
```

**Example 2:**

```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: Distances are sqrt(18), sqrt(26), sqrt(20). The two closest are (3,3) and (-2,4).
```

**Example 3:**

```
Input: points = [[0,0],[1,1],[2,2]], k = 1
Output: [[0,0]]
Explanation: The origin point itself has distance 0, which is the smallest.
```

## Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Function Signature

**Go:**

```go
func kClosest(points [][]int, k int) [][]int
```

**Python:**
```python
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
```
