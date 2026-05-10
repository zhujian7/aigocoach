# Longest Substring Without Repeating Characters

- **Difficulty**: Medium
- **Category**: Sliding Window
- **Topics**: string, hash table, sliding window
- **Link**: [NeetCode](https://neetcode.io/problems/longest-substring-without-duplicates) | [LeetCode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Description

Given a string `s`, find the length of the longest substring without repeating characters.

A substring is a contiguous non-empty sequence of characters within a string. The substring must not contain any duplicate characters.

## Examples

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Note that "pwke" is a subsequence and not a substring.
```

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.

## Function Signature

**Go:**

```go
func lengthOfLongestSubstring(s string) int
```

**Python:**
```python
def length_of_longest_substring(s: str) -> int:
```
