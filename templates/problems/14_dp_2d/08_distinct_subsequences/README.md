# Distinct Subsequences

- **Difficulty**: Hard
- **Category**: 2D Dynamic Programming
- **Topics**: dynamic programming, string
- **Link**: [NeetCode](https://neetcode.io/problems/distinct-subsequences) | [LeetCode 115](https://leetcode.com/problems/distinct-subsequences/)

## Description

Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equal `t`. A subsequence of a string is a new string formed by deleting some (or no) characters from the original string without disturbing the relative positions of the remaining characters. The test cases are generated so that the answer fits on a 32-bit signed integer.

## Examples

**Example 1:**

```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation: There are 3 ways to choose "rabbit" from "rabbbit" (by choosing which of the three 'b's to skip).
```

**Example 2:**

```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation: There are 5 distinct subsequences of "babgbag" that equal "bag".
```

**Example 3:**

```
Input: s = "aaa", t = "a"
Output: 3
Explanation: Each of the three 'a' characters forms a valid subsequence.
```

## Constraints

- `1 <= s.length, t.length <= 1000`
- `s` and `t` consist of English letters.

## Function Signature

**Go:**

```go
func numDistinct(s string, t string) int
```

**Python:**
```python
def num_distinct(s: str, t: str) -> int:
```
