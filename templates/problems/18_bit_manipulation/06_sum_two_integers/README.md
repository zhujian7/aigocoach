# Sum of Two Integers

- **Difficulty**: Medium
- **Category**: Bit Manipulation
- **Topics**: bit manipulation, math
- **Link**: [NeetCode](https://neetcode.io/problems/sum-of-two-integers) | [LeetCode 371](https://leetcode.com/problems/sum-of-two-integers/)

## Description

Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`. You must use bitwise operations to compute the sum.

## Examples

**Example 1:**

```
Input: a = 1, b = 2
Output: 3
Explanation: 1 + 2 = 3, computed using bitwise operations.
```

**Example 2:**

```
Input: a = 2, b = -1
Output: 1
Explanation: 2 + (-1) = 1, computed using bitwise operations.
```

**Example 3:**

```
Input: a = 0, b = 0
Output: 0
Explanation: 0 + 0 = 0.
```

## Constraints

- `-1000 <= a, b <= 1000`

## Function Signature

**Go:**

```go
func getSum(a int, b int) int
```

**Python:**
```python
def get_sum(a: int, b: int) -> int:
```
