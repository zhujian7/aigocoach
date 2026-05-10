# Permutation in String

- **Difficulty**: Medium
- **Category**: Sliding Window
- **Topics**: string, hash table, sliding window, two pointers
- **Link**: [NeetCode](https://neetcode.io/problems/permutation-string) | [LeetCode 567](https://leetcode.com/problems/permutation-in-string/)

## Description

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`. A permutation is a rearrangement of all the characters of a string.

## Examples

**Example 1:**

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba"), which is a substring of s2.
```

**Example 2:**

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
Explanation: No permutation of "ab" exists as a contiguous substring in s2.
```

**Example 3:**

```
Input: s1 = "aab", s2 = "ccccbaa"
Output: true
Explanation: s2 contains the permutation "baa" of s1 as a substring.
```

## Constraints

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

## Function Signature

**Go:**

```go
func checkInclusion(s1 string, s2 string) bool
```

**Python:**
```python
def check_inclusion(s1: str, s2: str) -> bool:
```
