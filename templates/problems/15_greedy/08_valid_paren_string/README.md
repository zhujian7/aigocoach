# Valid Parenthesis String

- **Difficulty**: Medium
- **Category**: Greedy
- **Topics**: string, greedy, dynamic programming
- **Link**: [NeetCode](https://neetcode.io/problems/valid-parenthesis-string) | [LeetCode 678](https://leetcode.com/problems/valid-parenthesis-string/)

## Description

Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` if `s` is valid. The following rules define a valid string: any left parenthesis `'('` must have a corresponding right parenthesis `')'`, any right parenthesis `')'` must have a corresponding left parenthesis `'('`, left parenthesis `'('` must go before the corresponding right parenthesis `')'`, and `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

## Examples

**Example 1:**

```
Input: s = "()"
Output: true
```

**Example 2:**

```
Input: s = "(*)"
Output: true
Explanation: '*' can be treated as empty, making the string "()" which is valid.
```

**Example 3:**

```
Input: s = "(*))"
Output: true
Explanation: '*' can be treated as '(', making the string "(())" which is valid.
```

## Constraints

- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`.

## Function Signature

**Go:**

```go
func checkValidString(s string) bool
```

**Python:**
```python
def check_valid_string(s: str) -> bool:
```
