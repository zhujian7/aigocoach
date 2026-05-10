# Burst Balloons

- **Difficulty**: Hard
- **Category**: 2D Dynamic Programming
- **Topics**: dynamic programming, interval DP
- **Link**: [NeetCode](https://neetcode.io/problems/burst-balloons) | [LeetCode 312](https://leetcode.com/problems/burst-balloons/)

## Description

You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by the array `nums`. You are asked to burst all the balloons. If you burst the `i`-th balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it. Return the maximum coins you can collect by bursting the balloons wisely.

## Examples

**Example 1:**

```
Input: nums = [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []. Coins: 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 15+120+24+8 = 167.
```

**Example 2:**

```
Input: nums = [1,5]
Output: 10
```

**Example 3:**

```
Input: nums = [5]
Output: 5
Explanation: Burst the only balloon to get 1*5*1 = 5 coins.
```

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `0 <= nums[i] <= 100`

## Function Signature

**Go:**

```go
func maxCoins(nums []int) int
```

**Python:**
```python
def max_coins(nums: List[int]) -> int:
```
