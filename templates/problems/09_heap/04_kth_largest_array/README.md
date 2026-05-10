# Kth Largest Element in an Array

- **Difficulty**: Medium
- **Category**: Heap
- **Topics**: min-heap, priority queue, quickselect
- **Link**: [NeetCode](https://neetcode.io/problems/kth-largest-element-in-an-array) | [LeetCode 215](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## Description

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element. You must solve it without sorting the entire array if aiming for optimal time complexity.

## Examples

**Example 1:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Explanation: The sorted array is [1,2,3,4,5,6]. The 2nd largest element is 5.
```

**Example 2:**

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
Explanation: The sorted array is [1,2,2,3,3,4,5,5,6]. The 4th largest element is 4.
```

**Example 3:**

```
Input: nums = [1], k = 1
Output: 1
Explanation: The only element is the 1st largest.
```

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Function Signature

**Go:**

```go
func findKthLargest(nums []int, k int) int
```

**Python:**
```python
def find_kth_largest(nums: List[int], k: int) -> int:
```
