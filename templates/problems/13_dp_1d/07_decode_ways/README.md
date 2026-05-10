# Decode Ways

- **Difficulty**: Medium
- **Category**: 1D Dynamic Programming
- **Topics**: dynamic programming, string
- **Link**: [NeetCode](https://neetcode.io/problems/decode-ways) | [LeetCode 91](https://leetcode.com/problems/decode-ways/)

## Description

A message containing letters from A-Z can be encoded into numbers using the mapping: 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26". Given a string `s` containing only digits, return the number of ways to decode it. The answer is guaranteed to fit in a 32-bit integer. Note that groupings like "06" are invalid because "06" is not a valid encoding (only "6" is valid). A digit string with a leading zero has no valid decodings.

## Examples

**Example 1:**

```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

**Example 2:**

```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

**Example 3:**

```
Input: s = "06"
Output: 0
Explanation: "06" cannot be decoded because leading zeros make the encoding invalid.
```

## Constraints

- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zeros.

## Function Signature

**Go:**

```go
func numDecodings(s string) int
```

**Python:**
```python
def num_decodings(s: str) -> int:
```
