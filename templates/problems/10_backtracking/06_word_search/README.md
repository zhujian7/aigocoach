# Word Search

- **Difficulty**: Medium
- **Category**: Backtracking
- **Topics**: backtracking, DFS, matrix
- **Link**: [NeetCode](https://neetcode.io/problems/search-for-word) | [LeetCode 79](https://leetcode.com/problems/word-search/)

## Description

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a single word path.

## Examples

**Example 1:**

![Example 1](assets/word2.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Explanation: The word "ABCCED" can be found following the path A(0,0)->B(0,1)->C(0,2)->C(1,2)->E(2,2)->D(2,1).
```

**Example 2:**

![Example 2](assets/word-1.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3:**

![Example 3](assets/word3.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
Explanation: The path would require reusing a cell, which is not allowed.
```

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

## Function Signature

**Go:**

```go
func exist(board [][]byte, word string) bool
```

**Python:**
```python
def exist(board: List[List[str]], word: str) -> bool:
```
