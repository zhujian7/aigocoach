# Surrounded Regions

- **Difficulty**: Medium
- **Category**: Graphs
- **Topics**: DFS, BFS, matrix, flood fill
- **Link**: [NeetCode](https://neetcode.io/problems/surrounded-regions) | [LeetCode 130](https://leetcode.com/problems/surrounded-regions/)

## Description

![surrounded-regions](assets/xogrid.jpg)

Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region. An `'O'` on the border of the board, and any `'O'` connected to it (directly or indirectly), is not considered surrounded and should not be flipped.

## Examples

**Example 1:**

```
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
Explanation: The bottom-left 'O' is on the border, so it is not flipped. The other 'O's are surrounded and are flipped to 'X'.
```

**Example 2:**

```
Input: board = [["X"]]
Output: [["X"]]
```

**Example 3:**

```
Input: board = [
  ["X","O","X"],
  ["X","O","X"],
  ["X","X","X"]
]
Output: [
  ["X","O","X"],
  ["X","O","X"],
  ["X","X","X"]
]
Explanation: The 'O' cells are connected to the top border, so they are not surrounded.
```

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`.

## Function Signature

**Go:**

```go
func solve(board [][]byte)
```

**Python:**
```python
def solve(board: List[List[str]]) -> None:
```
