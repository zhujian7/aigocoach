# Pow(x, n)

- **Difficulty**: Medium
- **Category**: Math & Geometry
- **Topics**: math, recursion, binary exponentiation
- **Link**: [NeetCode](https://neetcode.io/problems/pow-x-n) | [LeetCode 50](https://leetcode.com/problems/powx-n/)

## Description

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`). The function should handle negative exponents (e.g., `x^(-n) = 1 / x^n`) and should not simply loop `n` times, as `n` can be very large.

## Examples

**Example 1:**

```
Input: x = 2.00000, n = 10
Output: 1024.00000
Explanation: 2^10 = 1024.
```

**Example 2:**

```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^(-2) = 1 / 2^2 = 1/4 = 0.25.
```

**Example 3:**

```
Input: x = 2.10000, n = 3
Output: 9.26100
Explanation: 2.1^3 = 9.261.
```

## Constraints

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- `n` is an integer
- Either `x` is not zero or `n > 0`
- `-10^4 <= x^n <= 10^4`

## Function Signature

**Go:**

```go
func myPow(x float64, n int) float64
```

**Python:**
```python
def my_pow(x: float, n: int) -> float:
```
