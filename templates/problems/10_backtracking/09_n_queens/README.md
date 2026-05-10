# N-Queens

- **Difficulty**: Hard
- **Category**: Backtracking
- **Topics**: backtracking, recursion, constraint satisfaction
- **Link**: [NeetCode](https://neetcode.io/problems/n-queens) | [LeetCode 51](https://leetcode.com/problems/n-queens/)

## Description

![n-queens](assets/queens.jpg)

The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other. A queen can attack any piece on the same row, column, or diagonal.

Given an integer `n`, return all distinct solutions to the n-queens puzzle. Each solution contains a distinct board configuration of the n-queens placement, where `'Q'` indicates a queen and `'.'` indicates an empty space.

## Examples

**Example 1:**

```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
Explanation: There are two distinct solutions to the 4-queens puzzle.
```

**Example 2:**

```
Input: n = 1
Output: [["Q"]]
```

**Example 3:**

```
Input: n = 2
Output: []
Explanation: There is no solution for the 2-queens puzzle.
```

## Constraints

- `1 <= n <= 9`

## Function Signature

**Go:**

```go
func solveNQueens(n int) [][]string
```

**Python:**
```python
def solve_n_queens(n: int) -> List[List[str]]:
```
