# House Robber II

- **Difficulty**: Medium
- **Category**: 1D Dynamic Programming
- **Topics**: dynamic programming, array
- **Link**: [NeetCode](https://neetcode.io/problems/house-robber-ii) | [LeetCode 213](https://leetcode.com/problems/house-robber-ii/)

## Description

You are a professional robber planning to rob houses arranged in a circle. Each house has a certain amount of money stashed. Adjacent houses have security systems connected, and since the houses form a circle, the first house and the last house are also considered adjacent. Given an integer array `nums` representing the amount of money in each house, return the maximum amount you can rob without alerting the police (i.e., without robbing two adjacent houses).

## Examples

**Example 1:**

```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 0 and house 2 since they are adjacent in the circle. Rob house 1 (money = 3).
```

**Example 2:**

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 0 (money = 1) and house 2 (money = 3). Total = 4.
```

**Example 3:**

```
Input: nums = [1,2,3]
Output: 3
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## Function Signature

**Go:**

```go
func robII(nums []int) int
```

**Python:**
```python
def rob_ii(nums: List[int]) -> int:
```
