# Subsets II

- **Difficulty**: Medium
- **Category**: Backtracking
- **Topics**: backtracking, sorting, deduplication
- **Link**: [NeetCode](https://neetcode.io/problems/subsets-ii) | [LeetCode 90](https://leetcode.com/problems/subsets-ii/)

## Description

Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

Unlike the basic Subsets problem, the input array may contain duplicate values. You must ensure that no two subsets in the output are identical.

## Examples

**Example 1:**

```
Input: nums = [1, 2, 2]
Output: [[], [1], [2], [1,2], [2,2], [1,2,2]]
```

**Example 2:**

```
Input: nums = [0]
Output: [[], [0]]
```

**Example 3:**

```
Input: nums = [1, 1, 1]
Output: [[], [1], [1,1], [1,1,1]]
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Function Signature

**Go:**

```go
func subsetsWithDup(nums []int) [][]int
```

**Python:**
```python
def subsets_with_dup(nums: List[int]) -> List[List[int]]:
```
