# Best Time to Buy and Sell Stock

- **Difficulty**: Easy
- **Category**: Sliding Window
- **Topics**: array, dynamic programming
- **Link**: [NeetCode](https://neetcode.io/problems/buy-and-sell-crypto) | [LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

Note that you must buy before you sell, and you are only allowed to complete at most one transaction.

## Examples

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

**Example 3:**

```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5 - 1 = 4.
```

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Function Signature

**Go:**

```go
func maxProfit(prices []int) int
```

**Python:**
```python
def max_profit(prices: List[int]) -> int:
```
