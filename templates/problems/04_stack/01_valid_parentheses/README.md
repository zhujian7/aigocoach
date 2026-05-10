# Valid Parentheses

- **Difficulty**: Easy
- **Category**: Stack
- **Topics**: stack, string, hash map
- **Link**: [NeetCode](https://neetcode.io/problems/validate-parentheses) | [LeetCode 20](https://leetcode.com/problems/valid-parentheses/)

## Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples

**Example 1:**

```
Input: s = "()"
Output: true
```

**Example 2:**

```
Input: s = "()[]{}"
Output: true
```

**Example 3:**

```
Input: s = "(]"
Output: false
Explanation: The opening '(' does not match the closing ']'.
```

## Constraints

- `0 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`

## Function Signature

**Go:**

```go
func isValid(s string) bool
```

**Python:**
```python
def is_valid(s: str) -> bool:
```
