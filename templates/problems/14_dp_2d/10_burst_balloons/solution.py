from typing import List


def solve_max_coins(nums: List[int]) -> int:
    n = len(nums)
    vals = [1] + nums + [1]
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    for length in range(1, n + 1):
        for left in range(1, n - length + 2):
            right = left + length - 1
            for k in range(left, right + 1):
                coins = vals[left - 1] * vals[k] * vals[right + 1]
                coins += dp[left][k - 1] + dp[k + 1][right]
                if coins > dp[left][right]:
                    dp[left][right] = coins

    return dp[1][n]
