# Longest Palindromic Substring

- **Difficulty**: Medium
- **Category**: 1D Dynamic Programming
- **Topics**: dynamic programming, string, two pointers
- **Link**: [NeetCode](https://neetcode.io/problems/longest-palindromic-substring) | [LeetCode 5](https://leetcode.com/problems/longest-palindromic-substring/)

## Description

Given a string `s`, return the longest palindromic substring in `s`. A palindrome is a string that reads the same forward and backward. If there are multiple answers of the same length, return any one of them.

## Examples

**Example 1:**

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**

```
Input: s = "cbbd"
Output: "bb"
```

**Example 3:**

```
Input: s = "racecar"
Output: "racecar"
Explanation: The entire string is a palindrome.
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of only lowercase English letters.

## Function Signature

**Go:**

```go
func longestPalindrome(s string) string
```

**Python:**
```python
def longest_palindrome(s: str) -> str:
```
