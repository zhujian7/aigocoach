# Minimum Window Substring

- **Difficulty**: Hard
- **Category**: Sliding Window
- **Topics**: string, hash table, sliding window
- **Link**: [NeetCode](https://neetcode.io/problems/minimum-window-with-characters) | [LeetCode 76](https://leetcode.com/problems/minimum-window-substring/)

## Description

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique. A substring is a contiguous sequence of characters within the string.

## Examples

**Example 1:**

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3:**

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since s only has one 'a', no valid window exists.
```

## Constraints

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

## Function Signature

**Go:**

```go
func minWindow(s string, t string) string
```

**Python:**
```python
def min_window(s: str, t: str) -> str:
```
