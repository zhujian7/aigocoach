# House Robber

- **Difficulty**: Medium
- **Category**: 1D Dynamic Programming
- **Topics**: dynamic programming, array
- **Link**: [NeetCode](https://neetcode.io/problems/house-robber) | [LeetCode 198](https://leetcode.com/problems/house-robber/)

## Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. Adjacent houses have security systems connected, so if two adjacent houses are broken into on the same night, the police will be alerted. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Examples

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 0 (money = 1) and house 2 (money = 3). Total = 1 + 3 = 4.
```

**Example 2:**

```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 0 (money = 2), house 2 (money = 9), and house 4 (money = 1). Total = 12.
```

**Example 3:**

```
Input: nums = [100,1,100,1,100]
Output: 300
```

## Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Function Signature

**Go:**

```go
func rob(nums []int) int
```

**Python:**
```python
def rob(nums: List[int]) -> int:
```
