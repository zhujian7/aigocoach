# Encode and Decode Strings

- **Difficulty**: Medium
- **Category**: Arrays & Hashing
- **Topics**: string, design
- **Link**: [NeetCode](https://neetcode.io/problems/string-encode-and-decode) | [LeetCode 271](https://leetcode.com/problems/encode-and-decode-strings/)

## Description

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement `encode` and `decode` functions. The encoded string should be able to handle any possible input, including strings that contain special characters, delimiters, or are empty. The encoding must be lossless -- decoding the encoded string must produce the exact original list of strings.

## Examples

**Example 1:**

```
Input: ["hello","world"]
Output: ["hello","world"]
Explanation: encode(["hello","world"]) may produce "5#hello5#world", and decode("5#hello5#world") returns ["hello","world"].
```

**Example 2:**

```
Input: [""]
Output: [""]
Explanation: The list contains a single empty string and must be preserved through encoding and decoding.
```

**Example 3:**

```
Input: ["he:llo","wor#ld","foo;bar"]
Output: ["he:llo","wor#ld","foo;bar"]
Explanation: Special characters in the strings must be handled correctly. The encoding must not be confused by characters that look like delimiters.
```

## Constraints

- `0 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` contains any possible characters out of 256 valid ASCII characters.

## Function Signature

**Go:**

```go
func encode(strs []string) string
func decode(s string) []string
```

**Python:**
```python
def encode(strs: List[str]) -> str:
def decode(s: str) -> List[str]:
```
