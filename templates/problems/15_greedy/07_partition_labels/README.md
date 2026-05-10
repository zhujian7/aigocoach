# Partition Labels

- **Difficulty**: Medium
- **Category**: Greedy
- **Topics**: string, greedy, hash table, two pointers
- **Link**: [NeetCode](https://neetcode.io/problems/partition-labels) | [LeetCode 763](https://leetcode.com/problems/partition-labels/)

## Description

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`. Return a list of integers representing the size of these parts.

## Examples

**Example 1:**

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation: The partition is "ababcbaca", "defegde", "hijhklij". Each letter appears in at most one part. A partition like "ababcbacadefegde", "hijhklij" is incorrect because it splits s into fewer parts.
```

**Example 2:**

```
Input: s = "eccbbbbdec"
Output: [10]
Explanation: All characters are interleaved so the entire string is one partition.
```

**Example 3:**

```
Input: s = "abcdef"
Output: [1,1,1,1,1,1]
Explanation: Each character appears only once, so each character is its own partition.
```

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

## Function Signature

**Go:**

```go
func partitionLabels(s string) []int
```

**Python:**
```python
def partition_labels(s: str) -> List[int]:
```
