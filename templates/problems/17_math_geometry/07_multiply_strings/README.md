# Multiply Strings

- **Difficulty**: Medium
- **Category**: Math & Geometry
- **Topics**: math, string, simulation
- **Link**: [NeetCode](https://neetcode.io/problems/multiply-strings) | [LeetCode 43](https://leetcode.com/problems/multiply-strings/)

## Description

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string. You must not use any built-in big integer library or convert the inputs to integers directly. The multiplication must be performed digit by digit.

## Examples

**Example 1:**

```
Input: num1 = "2", num2 = "3"
Output: "6"
Explanation: 2 * 3 = 6.
```

**Example 2:**

```
Input: num1 = "123", num2 = "456"
Output: "56088"
Explanation: 123 * 456 = 56088.
```

**Example 3:**

```
Input: num1 = "0", num2 = "52"
Output: "0"
Explanation: Any number multiplied by 0 is 0.
```

## Constraints

- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only
- `num1` and `num2` do not contain any leading zero, except the number `0` itself

## Function Signature

**Go:**

```go
func multiply(num1 string, num2 string) string
```

**Python:**
```python
def multiply(num1: str, num2: str) -> str:
```
