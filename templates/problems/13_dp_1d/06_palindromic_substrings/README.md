# Palindromic Substrings

- **Difficulty**: Medium
- **Category**: 1D Dynamic Programming
- **Topics**: dynamic programming, string, two pointers
- **Link**: [NeetCode](https://neetcode.io/problems/palindromic-substrings) | [LeetCode 647](https://leetcode.com/problems/palindromic-substrings/)

## Description

Given a string `s`, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string. Note that substrings with different start or end indices are counted as different substrings even if they consist of the same characters.

## Examples

**Example 1:**

```
Input: s = "abc"
Output: 3
Explanation: Three palindromic substrings: "a", "b", "c".
```

**Example 2:**

```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic substrings: "a" (3 times), "aa" (2 times), "aaa" (1 time).
```

**Example 3:**

```
Input: s = "racecar"
Output: 10
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Function Signature

**Go:**

```go
func countSubstrings(s string) int
```

**Python:**
```python
def count_substrings(s: str) -> int:
```
