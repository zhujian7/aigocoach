# Happy Number

- **Difficulty**: Easy
- **Category**: Math & Geometry
- **Topics**: math, hash table, two pointers
- **Link**: [NeetCode](https://neetcode.io/problems/non-cyclical-number) | [LeetCode 202](https://leetcode.com/problems/happy-number/)

## Description

Write an algorithm to determine if a number `n` is happy. A happy number is defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals `1` (where it will stay), or it loops endlessly in a cycle which does not include `1`. Those numbers for which this process ends in `1` are happy.

Return `true` if `n` is a happy number, and `false` otherwise.

## Examples

**Example 1:**

```
Input: n = 19
Output: true
Explanation: 1^2 + 9^2 = 82 -> 8^2 + 2^2 = 68 -> 6^2 + 8^2 = 100 -> 1^2 + 0^2 + 0^2 = 1.
```

**Example 2:**

```
Input: n = 2
Output: false
Explanation: The sequence 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> ... enters a cycle and never reaches 1.
```

**Example 3:**

```
Input: n = 1
Output: true
Explanation: 1 is already 1.
```

## Constraints

- `1 <= n <= 2^31 - 1`

## Function Signature

**Go:**

```go
func isHappy(n int) bool
```

**Python:**
```python
def is_happy(n: int) -> bool:
```
