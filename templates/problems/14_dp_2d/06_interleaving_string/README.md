# Interleaving String

- **Difficulty**: Medium
- **Category**: 2D Dynamic Programming
- **Topics**: dynamic programming, string
- **Link**: [NeetCode](https://neetcode.io/problems/interleaving-string) | [LeetCode 97](https://leetcode.com/problems/interleaving-string/)

## Description

![interleaving-string](assets/interleave.jpg)

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`. An interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into substrings such that the concatenation of the substrings from `s` and `t` forms `s3`, and the relative order of characters within each original string is preserved.

## Examples

**Example 1:**

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One valid interleaving is: aa|dbbc|bc|a|c where characters from s1 and s2 alternate while preserving their relative order.
```

**Example 2:**

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
```

**Example 3:**

```
Input: s1 = "", s2 = "", s3 = ""
Output: true
```

## Constraints

- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`
- `s1`, `s2`, and `s3` consist of lowercase English letters.

## Function Signature

**Go:**

```go
func isInterleave(s1 string, s2 string, s3 string) bool
```

**Python:**
```python
def is_interleave(s1: str, s2: str, s3: str) -> bool:
```
