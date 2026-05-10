# Number of Islands

- **Difficulty**: Medium
- **Category**: Graphs
- **Topics**: DFS, BFS, matrix, flood fill
- **Link**: [NeetCode](https://neetcode.io/problems/count-number-of-islands) | [LeetCode 200](https://leetcode.com/problems/number-of-islands/)

## Description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

## Examples

**Example 1:**

```
Input: grid = [
  ["1","1","1"],
  ["0","1","0"],
  ["1","1","1"]
]
Output: 1
```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

**Example 3:**

```
Input: grid = [
  ["1","0"],
  ["0","1"]
]
Output: 2
Explanation: The two 1s are diagonal, not adjacent, so they form separate islands.
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Function Signature

**Go:**

```go
func numIslands(grid [][]byte) int
```

**Python:**
```python
def num_islands(grid: List[List[str]]) -> int:
```
