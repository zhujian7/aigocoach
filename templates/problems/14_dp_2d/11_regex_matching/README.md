# Regular Expression Matching

- **Difficulty**: Hard
- **Category**: 2D Dynamic Programming
- **Topics**: dynamic programming, string, recursion
- **Link**: [NeetCode](https://neetcode.io/problems/regular-expression-matching) | [LeetCode 10](https://leetcode.com/problems/regular-expression-matching/)

## Description

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where `.` matches any single character and `*` matches zero or more of the preceding element. The matching should cover the entire input string (not partial).

## Examples

**Example 1:**

```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:**

```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element 'a'. Therefore, by repeating 'a' twice, it matches "aa".
```

**Example 3:**

```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means zero or more of any character, which matches "ab".
```

## Constraints

- `1 <= s.length <= 20`
- `1 <= p.length <= 20`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `.`, and `*`.
- It is guaranteed for each appearance of `*`, there will be a preceding valid character to match.

## Function Signature

**Go:**

```go
func isMatch(s string, p string) bool
```

**Python:**
```python
def is_match(s: str, p: str) -> bool:
```
