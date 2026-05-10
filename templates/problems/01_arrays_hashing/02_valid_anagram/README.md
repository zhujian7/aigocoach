# Valid Anagram

- **Difficulty**: Easy
- **Category**: Arrays & Hashing
- **Topics**: string, hash table, sorting
- **Link**: [NeetCode](https://neetcode.io/problems/is-anagram) | [LeetCode 242](https://leetcode.com/problems/valid-anagram/)

## Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

## Examples

**Example 1:**

```
Input: s = "anagram", t = "nagaram"
Output: true
Explanation: "nagaram" is formed by rearranging all letters of "anagram".
```

**Example 2:**

```
Input: s = "rat", t = "car"
Output: false
Explanation: The letters in "rat" cannot be rearranged to form "car".
```

**Example 3:**

```
Input: s = "", t = ""
Output: true
```

## Constraints

- `0 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Function Signature

**Go:**

```go
func isAnagram(s string, t string) bool
```

**Python:**
```python
def is_anagram(s: str, t: str) -> bool:
```
