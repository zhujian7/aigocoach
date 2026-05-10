# Reverse Integer

- **Difficulty**: Medium
- **Category**: Bit Manipulation
- **Topics**: math
- **Link**: [NeetCode](https://neetcode.io/problems/reverse-integer) | [LeetCode 7](https://leetcode.com/problems/reverse-integer/)

## Description

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

## Examples

**Example 1:**

```
Input: x = 123
Output: 321
Explanation: Reversing the digits of 123 gives 321.
```

**Example 2:**

```
Input: x = -123
Output: -321
Explanation: Reversing the digits of -123 gives -321 (the sign is preserved).
```

**Example 3:**

```
Input: x = 120
Output: 21
Explanation: Reversing the digits of 120 gives 21 (trailing zeros are dropped).
```

## Constraints

- `-2^31 <= x <= 2^31 - 1`

## Function Signature

**Go:**

```go
func reverse(x int) int
```

**Python:**
```python
def reverse(x: int) -> int:
```
