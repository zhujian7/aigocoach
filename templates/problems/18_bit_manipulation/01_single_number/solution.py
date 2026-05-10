from typing import List


def solve_single_number(nums: List[int]) -> int:
    result = 0
    for n in nums:
        result ^= n
    return result
