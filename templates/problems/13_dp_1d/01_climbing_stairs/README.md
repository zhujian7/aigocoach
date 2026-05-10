# Climbing Stairs

- **Difficulty**: Easy
- **Category**: 1D Dynamic Programming
- **Topics**: dynamic programming, fibonacci
- **Link**: [NeetCode](https://neetcode.io/problems/climbing-stairs) | [LeetCode 70](https://leetcode.com/problems/climbing-stairs/)

## Description

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. Return the number of distinct ways you can climb to the top.

## Examples

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top: 1+1 and 2.
```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways: 1+1+1, 1+2, and 2+1.
```

**Example 3:**

```
Input: n = 5
Output: 8
```

## Constraints

- `1 <= n <= 45`

## Function Signature

**Go:**

```go
func climbStairs(n int) int
```

**Python:**
```python
def climb_stairs(n: int) -> int:
```
