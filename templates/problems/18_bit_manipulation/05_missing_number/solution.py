from typing import List


def solve_missing_number(nums: List[int]) -> int:
    result = len(nums)
    for i, v in enumerate(nums):
        result ^= i ^ v
    return result
