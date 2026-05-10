# Maximum Subarray

- **Difficulty**: Medium
- **Category**: Greedy
- **Topics**: array, dynamic programming, greedy, Kadane's algorithm
- **Link**: [NeetCode](https://neetcode.io/problems/maximum-subarray) | [LeetCode 53](https://leetcode.com/problems/maximum-subarray/)

## Description

Given an integer array `nums`, find the subarray with the largest sum, and return its sum. A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

**Example 2:**

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

**Example 3:**

```
Input: nums = [-1]
Output: -1
Explanation: The subarray [-1] has the largest sum -1. Even though it's negative, we must pick at least one element.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Function Signature

**Go:**

```go
func maxSubArray(nums []int) int
```

**Python:**
```python
def max_sub_array(nums: List[int]) -> int:
```
