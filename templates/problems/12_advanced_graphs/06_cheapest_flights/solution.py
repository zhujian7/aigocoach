from typing import List


def solve_find_cheapest_price(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    if src == dst:
        return 0
    prices = [float('inf')] * n
    prices[src] = 0

    for _ in range(k + 1):
        tmp = prices[:]
        for frm, to, cost in flights:
            if prices[frm] == float('inf'):
                continue
            if prices[frm] + cost < tmp[to]:
                tmp[to] = prices[frm] + cost
        prices = tmp

    return -1 if prices[dst] == float('inf') else prices[dst]
