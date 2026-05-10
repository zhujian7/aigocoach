from typing import List


def solve_max_product(nums: List[int]) -> int:
    if not nums:
        return 0
    result = nums[0]
    cur_max, cur_min = nums[0], nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(nums[i], cur_max * nums[i])
        cur_min = min(nums[i], cur_min * nums[i])
        result = max(result, cur_max)
    return result
