# Coin Change

- **Difficulty**: Medium
- **Category**: 1D Dynamic Programming
- **Topics**: dynamic programming, breadth-first search
- **Link**: [NeetCode](https://neetcode.io/problems/coin-change) | [LeetCode 322](https://leetcode.com/problems/coin-change/)

## Description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of each kind of coin.

## Examples

**Example 1:**

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1.
```

**Example 2:**

```
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount 3 cannot be made with only coins of denomination 2.
```

**Example 3:**

```
Input: coins = [1], amount = 0
Output: 0
```

## Constraints

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Function Signature

**Go:**

```go
func coinChange(coins []int, amount int) int
```

**Python:**
```python
def coin_change(coins: List[int], amount: int) -> int:
```
