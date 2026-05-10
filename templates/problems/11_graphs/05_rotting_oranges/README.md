# Rotting Oranges

- **Difficulty**: Medium
- **Category**: Graphs
- **Topics**: BFS, multi-source BFS, matrix
- **Link**: [NeetCode](https://neetcode.io/problems/rotting-fruit) | [LeetCode 994](https://leetcode.com/problems/rotting-oranges/)

## Description

![rotting-oranges](assets/oranges.png)

You are given an `m x n` grid where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

## Examples

**Example 1:**

```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:**

```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom-left corner is never reached by any rotten orange.
```

**Example 3:**

```
Input: grid = [[0,2]]
Output: 0
Explanation: There are no fresh oranges, so 0 minutes are needed.
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

## Function Signature

**Go:**

```go
func orangesRotting(grid [][]int) int
```

**Python:**
```python
def oranges_rotting(grid: List[List[int]]) -> int:
```
