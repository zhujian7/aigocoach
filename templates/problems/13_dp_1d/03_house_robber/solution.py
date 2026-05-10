from typing import List


def solve_rob(nums: List[int]) -> int:
    if not nums:
        return 0
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr
