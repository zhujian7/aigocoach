# Max Area of Island

- **Difficulty**: Medium
- **Category**: Graphs
- **Topics**: DFS, BFS, matrix, flood fill
- **Link**: [NeetCode](https://neetcode.io/problems/max-area-of-island) | [LeetCode 695](https://leetcode.com/problems/max-area-of-island/)

## Description

![max-area-of-island](assets/maxarea1-grid.jpg)

You are given an `m x n` binary matrix `grid`. An island is a group of `1`s (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value `1` in the island. Return the maximum area of an island in `grid`. If there is no island, return `0`.

## Examples

**Example 1:**

```
Input: grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The largest island has area 6 (the connected component in the bottom-right area).
```

**Example 2:**

```
Input: grid = [[0,0,0],[0,0,0]]
Output: 0
```

**Example 3:**

```
Input: grid = [[1,1],[1,1]]
Output: 4
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is either `0` or `1`.

## Function Signature

**Go:**

```go
func maxAreaOfIsland(grid [][]int) int
```

**Python:**
```python
def max_area_of_island(grid: List[List[int]]) -> int:
```
