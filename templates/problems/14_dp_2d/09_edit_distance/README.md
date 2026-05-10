# Edit Distance

- **Difficulty**: Medium
- **Category**: 2D Dynamic Programming
- **Topics**: dynamic programming, string
- **Link**: [NeetCode](https://neetcode.io/problems/edit-distance) | [LeetCode 72](https://leetcode.com/problems/edit-distance/)

## Description

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. You have the following three operations permitted on a word: insert a character, delete a character, or replace a character.

## Examples

**Example 1:**

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: horse -> rorse (replace 'h' with 'r') -> rose (remove 'r') -> ros (remove 'e').
```

**Example 2:**

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: intention -> inention (remove 't') -> enention (replace 'i' with 'e') -> exention (replace 'n' with 'x') -> exection (replace 'n' with 'c') -> execution (insert 'u').
```

**Example 3:**

```
Input: word1 = "", word2 = "abc"
Output: 3
Explanation: Insert three characters to transform the empty string into "abc".
```

## Constraints

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

## Function Signature

**Go:**

```go
func minDistance(word1 string, word2 string) int
```

**Python:**
```python
def min_distance(word1: str, word2: str) -> int:
```
