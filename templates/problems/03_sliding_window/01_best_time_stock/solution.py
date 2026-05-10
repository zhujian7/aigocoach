from typing import List


def solve_max_profit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > max_profit:
            max_profit = p - min_price
    return max_profit
