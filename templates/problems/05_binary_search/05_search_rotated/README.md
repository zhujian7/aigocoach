# Search in Rotated Sorted Array

- **Difficulty**: Medium
- **Category**: Binary Search
- **Topics**: binary search, array
- **Link**: [NeetCode](https://neetcode.io/problems/find-target-in-rotated-sorted-array) | [LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Description

There is an integer array `nums` sorted in ascending order (with distinct values). Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`. You must write an algorithm with O(log n) runtime complexity.

## Examples

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Explanation: 0 is found at index 4.
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Explanation: 3 is not in the array, so return -1.
```

**Example 3:**

```
Input: nums = [1], target = 1
Output: 0
Explanation: The array has one element equal to the target.
```

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique
- `nums` is an ascending array that is possibly rotated
- `-10^4 <= target <= 10^4`

## Function Signature

**Go:**

```go
func searchRotated(nums []int, target int) int
```

**Python:**
```python
def search_rotated(nums: List[int], target: int) -> int:
```
