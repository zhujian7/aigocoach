# Longest Increasing Subsequence

- **Difficulty**: Medium
- **Category**: 1D Dynamic Programming
- **Topics**: dynamic programming, binary search
- **Link**: [NeetCode](https://neetcode.io/problems/longest-increasing-subsequence) | [LeetCode 300](https://leetcode.com/problems/longest-increasing-subsequence/)

## Description

Given an integer array `nums`, return the length of the longest strictly increasing subsequence. A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

## Examples

**Example 1:**

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

**Example 2:**

```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Example 3:**

```
Input: nums = [7,7,7,7,7]
Output: 1
```

## Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

## Function Signature

**Go:**

```go
func lengthOfLIS(nums []int) int
```

**Python:**
```python
def length_of_lis(nums: List[int]) -> int:
```
