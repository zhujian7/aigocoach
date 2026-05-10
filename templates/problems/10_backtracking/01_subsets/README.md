# Subsets

- **Difficulty**: Medium
- **Category**: Backtracking
- **Topics**: backtracking, bit manipulation, recursion
- **Link**: [NeetCode](https://neetcode.io/problems/subsets) | [LeetCode 78](https://leetcode.com/problems/subsets/)

## Description

Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets, and the subsets can be returned in any order.

For example, given `nums = [1, 2, 3]`, the output should include all 8 subsets: the empty set, each individual element, each pair, and the full set.

## Examples

**Example 1:**

```
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

**Example 2:**

```
Input: nums = [0]
Output: [[], [0]]
```

**Example 3:**

```
Input: nums = [1, 2]
Output: [[], [1], [2], [1,2]]
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are unique.

## Function Signature

**Go:**

```go
func subsets(nums []int) [][]int
```

**Python:**
```python
def subsets(nums: List[int]) -> List[List[int]]:
```
