# Design Add and Search Words Data Structure

- **Difficulty**: Medium
- **Category**: Tries
- **Topics**: trie, DFS, backtracking, wildcard matching
- **Link**: [NeetCode](https://neetcode.io/problems/design-word-search-data-structure) | [LeetCode 211](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

## Description

Design a data structure that supports adding new words and finding if a string matches any previously added string. The data structure should support the following operations:

- `AddWord(word string)` adds `word` to the data structure so it can be matched later.
- `Search(word string) bool` returns `true` if there is any string in the data structure that matches `word`. The `word` may contain dots `'.'` where each dot can be matched with any letter.

## Examples

**Example 1:**

```
Input:
  NewWordDictionary()
  AddWord("bad")
  AddWord("dad")
  AddWord("mad")
  Search("pad")  -> false
  Search("bad")  -> true
  Search(".ad")  -> true
  Search("b..")  -> true

Explanation: "pad" was never added. "bad" matches exactly. ".ad" matches "bad", "dad", or "mad" since '.' matches any character. "b.." matches "bad".
```

**Example 2:**

```
Input:
  NewWordDictionary()
  AddWord("a")
  Search(".")   -> true
  Search("a")   -> true
  Search("..")  -> false

Explanation: "." matches "a" (single character). ".." requires a two-character word but only "a" (length 1) was added.
```

## Constraints

- `1 <= word.length <= 25`
- `word` in `AddWord` consists of lowercase English letters.
- `word` in `Search` consists of lowercase English letters or `'.'`.
- At most `10^4` calls will be made to `AddWord` and `Search`.

## Function Signature

**Go:**

```go
type WordDictionary struct {
    Root *TrieNode
}

func NewWordDictionary() WordDictionary

func (wd *WordDictionary) AddWord(word string)

func (wd *WordDictionary) Search(word string) bool
```

**Python:**
```python
class WordDictionary
def __init__(self):
def add_word(self, word: str) -> None:
def search(self, word: str) -> bool:
```
