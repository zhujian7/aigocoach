# Longest Consecutive Sequence

- **Difficulty**: Medium
- **Category**: Arrays & Hashing
- **Topics**: array, hash table, union find
- **Link**: [NeetCode](https://neetcode.io/problems/longest-consecutive-sequence) | [LeetCode 128](https://leetcode.com/problems/longest-consecutive-sequence/)

## Description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

A consecutive sequence is a sequence of elements where each element is exactly 1 greater than the previous element. The elements do not need to be adjacent in the original array.

## Examples

**Example 1:**

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

**Example 2:**

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore its length is 9.
```

**Example 3:**

```
Input: nums = []
Output: 0
```

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Function Signature

**Go:**

```go
func longestConsecutive(nums []int) int
```

**Python:**
```python
def longest_consecutive(nums: List[int]) -> int:
```
