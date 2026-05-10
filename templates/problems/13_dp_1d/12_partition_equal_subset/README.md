# Partition Equal Subset Sum

- **Difficulty**: Medium
- **Category**: 1D Dynamic Programming
- **Topics**: dynamic programming, 0/1 knapsack
- **Link**: [NeetCode](https://neetcode.io/problems/partition-equal-subset-sum) | [LeetCode 416](https://leetcode.com/problems/partition-equal-subset-sum/)

## Description

Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal, or `false` otherwise.

## Examples

**Example 1:**

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1,5,5] and [11], both summing to 11.
```

**Example 2:**

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

**Example 3:**

```
Input: nums = [1,2,3,4,5,6,7]
Output: true
Explanation: The array can be partitioned as [1,6,7] and [2,3,4,5], both summing to 14.
```

## Constraints

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

## Function Signature

**Go:**

```go
func canPartition(nums []int) bool
```

**Python:**
```python
def can_partition(nums: List[int]) -> bool:
```
