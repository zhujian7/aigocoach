# Implement Trie (Prefix Tree)

- **Difficulty**: Medium
- **Category**: Tries
- **Topics**: trie, prefix tree, hash map, string
- **Link**: [NeetCode](https://neetcode.io/problems/implement-prefix-tree) | [LeetCode 208](https://leetcode.com/problems/implement-trie-prefix-tree/)

## Description

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. Implement the `Trie` struct with the following operations:

- `NewTrie()` initializes the trie object.
- `Insert(word string)` inserts the string `word` into the trie.
- `Search(word string) bool` returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `StartsWith(prefix string) bool` returns `true` if there is a previously inserted string that has the prefix `prefix`, and `false` otherwise.

## Examples

**Example 1:**

```
Input:
  NewTrie()
  Insert("apple")
  Search("apple")   -> true
  Search("app")     -> false
  StartsWith("app") -> true
  Insert("app")
  Search("app")     -> true

Explanation: After inserting "apple", searching for "apple" returns true but "app" returns false since it was not inserted as a complete word. However, StartsWith("app") returns true because "apple" has that prefix. After inserting "app", searching for "app" returns true.
```

**Example 2:**

```
Input:
  NewTrie()
  Insert("the")
  Insert("then")
  Insert("them")
  Search("the")      -> true
  Search("they")     -> false
  StartsWith("the")  -> true
  StartsWith("thx")  -> false

Explanation: Words "the", "then", and "them" share the prefix "the". Searching for "they" fails because it was never inserted.
```

## Constraints

- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters.
- At most `3 * 10^4` calls in total will be made to `Insert`, `Search`, and `StartsWith`.

## Function Signature

**Go:**

```go
type Trie struct {
    Root *TrieNode
}

func NewTrie() Trie

func (t *Trie) Insert(word string)

func (t *Trie) Search(word string) bool

func (t *Trie) StartsWith(prefix string) bool
```

**Python:**
```python
class Trie
def __init__(self):
def insert(self, word: str) -> None:
def search(self, word: str) -> bool:
def starts_with(self, prefix: str) -> bool:
```
