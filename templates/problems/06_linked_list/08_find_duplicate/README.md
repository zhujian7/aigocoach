# Find the Duplicate Number

- **Difficulty**: Medium
- **Category**: Linked List
- **Topics**: Floyd's cycle detection, two pointers, array
- **Link**: [NeetCode](https://neetcode.io/problems/find-the-duplicate-number) | [LeetCode 287](https://leetcode.com/problems/find-the-duplicate-number/)

## Description

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, there is only one repeated number in `nums`. Return this repeated number.

You must solve the problem without modifying the array `nums` and using only constant extra space.

## Examples

**Example 1:**

```
Input: nums = [1,3,4,2,2]
Output: 2
Explanation: The number 2 appears twice in the array.
```

**Example 2:**

```
Input: nums = [3,1,3,4,2]
Output: 3
Explanation: The number 3 appears twice in the array.
```

**Example 3:**

```
Input: nums = [1,1]
Output: 1
Explanation: The only possible number is 1, and it is duplicated.
```

## Constraints

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only once except for precisely one integer which appears two or more times

## Function Signature

**Go:**

```go
func findDuplicate(nums []int) int
```

**Python:**
```python
def find_duplicate(nums: List[int]) -> int:
```
