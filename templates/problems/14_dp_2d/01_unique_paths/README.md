# Unique Paths

- **Difficulty**: Medium
- **Category**: 2D Dynamic Programming
- **Topics**: dynamic programming, math, combinatorics
- **Link**: [NeetCode](https://neetcode.io/problems/unique-paths) | [LeetCode 62](https://leetcode.com/problems/unique-paths/)

## Description

![unique-paths](assets/robot_maze.png)

There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m-1][n-1]`). The robot can only move either down or right at any point in time. Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

## Examples

**Example 1:**

```
Input: m = 3, n = 7
Output: 28
```

**Example 2:**

```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner: Right -> Down -> Down, Down -> Down -> Right, Down -> Right -> Down.
```

**Example 3:**

```
Input: m = 1, n = 1
Output: 1
```

## Constraints

- `1 <= m, n <= 100`

## Function Signature

**Go:**

```go
func uniquePaths(m int, n int) int
```

**Python:**
```python
def unique_paths(m: int, n: int) -> int:
```
