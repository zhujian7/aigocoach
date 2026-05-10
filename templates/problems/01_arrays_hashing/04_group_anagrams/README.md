# Group Anagrams

- **Difficulty**: Medium
- **Category**: Arrays & Hashing
- **Topics**: string, hash table, sorting
- **Link**: [NeetCode](https://neetcode.io/problems/anagram-groups) | [LeetCode 49](https://leetcode.com/problems/group-anagrams/)

## Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

## Examples

**Example 1:**

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation: "eat", "tea", and "ate" are anagrams of each other, as are "tan" and "nat". "bat" has no anagram in the list.
```

**Example 2:**

```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**

```
Input: strs = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Function Signature

**Go:**

```go
func groupAnagrams(strs []string) [][]string
```

**Python:**
```python
def group_anagrams(strs: List[str]) -> List[List[str]]:
```
