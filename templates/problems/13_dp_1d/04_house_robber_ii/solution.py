from typing import List


def solve_rob_ii(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    return max(_rob_range(nums, 0, n - 2), _rob_range(nums, 1, n - 1))


def _rob_range(nums: List[int], lo: int, hi: int) -> int:
    prev, curr = 0, 0
    for i in range(lo, hi + 1):
        prev, curr = curr, max(curr, prev + nums[i])
    return curr
