# Min Cost Climbing Stairs

- **Difficulty**: Easy
- **Category**: 1D Dynamic Programming
- **Topics**: dynamic programming, array
- **Link**: [NeetCode](https://neetcode.io/problems/min-cost-climbing-stairs) | [LeetCode 746](https://leetcode.com/problems/min-cost-climbing-stairs/)

## Description

You are given an integer array `cost` where `cost[i]` is the cost of the `i`-th step on a staircase. Once you pay the cost, you can either climb one or two steps. You can start from the step with index 0 or the step with index 1. Return the minimum cost to reach the top of the floor (beyond the last step).

## Examples

**Example 1:**

```
Input: cost = [10,15,20]
Output: 15
Explanation: Start at index 1, pay 15, and climb two steps to reach the top.
```

**Example 2:**

```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Start at index 0 and follow the path with indices 0, 2, 4, 6, 7, 9 for a total cost of 6.
```

## Constraints

- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`

## Function Signature

**Go:**

```go
func minCostClimbingStairs(cost []int) int
```

**Python:**
```python
def min_cost_climbing_stairs(cost: List[int]) -> int:
```
