# Longest Repeating Character Replacement

- **Difficulty**: Medium
- **Category**: Sliding Window
- **Topics**: string, hash table, sliding window
- **Link**: [NeetCode](https://neetcode.io/problems/longest-repeating-substring-with-replacement) | [LeetCode 424](https://leetcode.com/problems/longest-repeating-character-replacement/)

## Description

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English letter. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Examples

**Example 1:**

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa. The entire string becomes "BBBB" or "AAAA", with length 4.
```

**Example 2:**

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'B' at index 3 with 'A'. The substring "AABA" has length 4 with all same characters.
```

**Example 3:**

```
Input: s = "AAAA", k = 0
Output: 4
Explanation: No replacements needed. The entire string already consists of the same character.
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Function Signature

**Go:**

```go
func characterReplacement(s string, k int) int
```

**Python:**
```python
def character_replacement(s: str, k: int) -> int:
```
