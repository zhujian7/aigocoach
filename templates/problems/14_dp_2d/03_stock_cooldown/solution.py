from typing import List


def solve_max_profit_cooldown(prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0
    held, sold, rest = -prices[0], 0, 0
    for i in range(1, len(prices)):
        prev_sold = sold
        sold = held + prices[i]
        held = max(held, rest - prices[i])
        rest = max(rest, prev_sold)
    return max(sold, rest)
