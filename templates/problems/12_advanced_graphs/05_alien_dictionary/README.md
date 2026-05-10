# Alien Dictionary

- **Difficulty**: Hard
- **Category**: Advanced Graphs
- **Topics**: topological sort, BFS, graph, string
- **Link**: [NeetCode](https://neetcode.io/problems/foreign-dictionary) | [LeetCode 269](https://leetcode.com/problems/alien-dictionary/) | [LintCode 892](https://www.lintcode.com/problem/892/)

## Description

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are sorted lexicographically by the rules of this new language.

Derive the order of letters in this language. If the order is invalid (i.e., there is a cycle or contradiction), return an empty string `""`. If there are multiple valid orderings, return any of them.

## Examples

**Example 1:**

```
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

**Example 2:**

```
Input: words = ["z","x"]
Output: "zx"
```

**Example 3:**

```
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid because 'z' must come both before and after 'x'.
```

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of only lowercase English letters.

## Function Signature

**Go:**

```go
func alienOrder(words []string) string
```

**Python:**
```python
def alien_order(words: List[str]) -> str:
```
