# Swim in Rising Water

- **Difficulty**: Hard
- **Category**: Advanced Graphs
- **Topics**: Dijkstra's algorithm, heap, binary search, BFS
- **Link**: [NeetCode](https://neetcode.io/problems/swim-in-rising-water) | [LeetCode 778](https://leetcode.com/problems/swim-in-rising-water/)

## Description

You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`.

The rain starts to fall. At time `t`, the depth of the water everywhere is `t`. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares is at most `t`. You can swim an infinite distance in zero time, but you must stay within the grid.

You start at the top-left square `(0, 0)`. What is the least time until you can reach the bottom-right square `(n - 1, n - 1)`?

## Examples

**Example 1:**

![Example 1](assets/swim1-grid.jpg)

```
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation: At time 3, you can swim from (0,0) to (1,0) to (1,1). All elevations are <= 3.
```

**Example 2:**

![Example 2](assets/swim2-grid-1.jpg)

```
Input: grid = [
  [0,1,2,3,4],
  [24,23,22,21,5],
  [12,13,14,15,16],
  [11,17,18,19,20],
  [10,9,8,7,6]
]
Output: 16
Explanation: The optimal path goes along the right side and bottom, with maximum elevation 16.
```

**Example 3:**

```
Input: grid = [[0]]
Output: 0
```

## Constraints

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] < n^2`
- Each value in `grid` is unique.

## Function Signature

**Go:**

```go
func swimInWater(grid [][]int) int
```

**Python:**
```python
def swim_in_water(grid: List[List[int]]) -> int:
```
