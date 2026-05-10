# Word Ladder

- **Difficulty**: Hard
- **Category**: Graphs
- **Topics**: BFS, string, hash set
- **Link**: [NeetCode](https://neetcode.io/problems/word-ladder) | [LeetCode 127](https://leetcode.com/problems/word-ladder/)

## Description

A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.

## Examples

**Example 1:**

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog" (5 words in the sequence).
```

**Example 2:**

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, so no valid transformation exists.
```

**Example 3:**

```
Input: beginWord = "hot", endWord = "dot", wordList = ["dot"]
Output: 2
Explanation: "hot" -> "dot" (2 words in the sequence).
```

## Constraints

- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- `beginWord != endWord`
- All the words in `wordList` are unique.

## Function Signature

**Go:**

```go
func ladderLength(beginWord string, endWord string, wordList []string) int
```

**Python:**
```python
def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
```
