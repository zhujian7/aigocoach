# Permutations

- **Difficulty**: Medium
- **Category**: Backtracking
- **Topics**: backtracking, recursion, permutation
- **Link**: [NeetCode](https://neetcode.io/problems/permutations) | [LeetCode 46](https://leetcode.com/problems/permutations/)

## Description

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

A permutation is a rearrangement of all the elements of the array. For an array of length `n`, there are `n!` total permutations.

## Examples

**Example 1:**

```
Input: nums = [1, 2, 3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

**Example 2:**

```
Input: nums = [1]
Output: [[1]]
```

**Example 3:**

```
Input: nums = [0, 1]
Output: [[0,1], [1,0]]
```

## Constraints

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are unique.

## Function Signature

**Go:**

```go
func permute(nums []int) [][]int
```

**Python:**
```python
def permute(nums: List[int]) -> List[List[int]]:
```
