# Palindrome Partitioning

- **Difficulty**: Medium
- **Category**: Backtracking
- **Topics**: backtracking, string, palindrome, dynamic programming
- **Link**: [NeetCode](https://neetcode.io/problems/palindrome-partitioning) | [LeetCode 131](https://leetcode.com/problems/palindrome-partitioning/)

## Description

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitionings of `s`.

A palindrome is a string that reads the same forward and backward. Each partitioning must use every character of the string exactly once.

## Examples

**Example 1:**

```
Input: s = "aab"
Output: [["a","a","b"], ["aa","b"]]
```

**Example 2:**

```
Input: s = "a"
Output: [["a"]]
```

**Example 3:**

```
Input: s = "aaa"
Output: [["a","a","a"], ["a","aa"], ["aa","a"], ["aaa"]]
```

## Constraints

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

## Function Signature

**Go:**

```go
func partition(s string) [][]string
```

**Python:**
```python
def partition(s: str) -> List[List[str]]:
```
