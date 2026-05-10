# Word Search II

- **Difficulty**: Hard
- **Category**: Tries
- **Topics**: trie, backtracking, DFS, matrix
- **Link**: [NeetCode](https://neetcode.io/problems/search-for-word-ii) | [LeetCode 212](https://leetcode.com/problems/word-search-ii/)

## Description

Given an `m x n` board of characters and a list of strings `words`, return all words on the board. Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a single word.

## Examples

**Example 1:**

![Example 1](assets/search1.jpg)

```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Explanation: "eat" can be formed starting at board[1][2] -> board[1][1] -> board[0][1]. "oath" can be formed starting at board[0][0] -> board[0][1] -> board[1][1] -> board[1][0]. "pea" and "rain" cannot be formed.
```

**Example 2:**

![Example 2](assets/search2.jpg)

```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
Explanation: "abcb" would require revisiting the 'b' cell, which is not allowed.
```

**Example 3:**

```
Input: board = [["a"]], words = ["a"]
Output: ["a"]
Explanation: The single cell matches the single-character word.
```

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 12`
- `board[i][j]` is a lowercase English letter.
- `1 <= words.length <= 3 * 10^4`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- All the strings of `words` are unique.

## Function Signature

**Go:**

```go
func findWords(board [][]byte, words []string) []string
```

**Python:**
```python
def find_words(board: List[List[str]], words: List[str]) -> List[str]:
```
