# Target Sum

- **Difficulty**: Medium
- **Category**: 2D Dynamic Programming
- **Topics**: dynamic programming, 0/1 knapsack
- **Link**: [NeetCode](https://neetcode.io/problems/target-sum) | [LeetCode 494](https://leetcode.com/problems/target-sum/)

## Description

You are given an integer array `nums` and an integer `target`. You want to build an expression out of `nums` by adding one of the symbols '+' or '-' before each integer in `nums` and then concatenate all the integers. Return the number of different expressions that you can build which evaluate to `target`.

## Examples

**Example 1:**

```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum equal to 3: -1+1+1+1+1=3, +1-1+1+1+1=3, +1+1-1+1+1=3, +1+1+1-1+1=3, +1+1+1+1-1=3.
```

**Example 2:**

```
Input: nums = [1], target = 1
Output: 1
```

**Example 3:**

```
Input: nums = [1], target = 2
Output: 0
Explanation: It is impossible to reach target 2 with a single element of value 1.
```

## Constraints

- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`
- `0 <= sum(nums[i]) <= 1000`
- `-1000 <= target <= 1000`

## Function Signature

**Go:**

```go
func findTargetSumWays(nums []int, target int) int
```

**Python:**
```python
def find_target_sum_ways(nums: List[int], target: int) -> int:
```
