from typing import List


def solve_max_sub_array(nums: List[int]) -> int:
    max_sum = nums[0]
    cur_sum = nums[0]
    for i in range(1, len(nums)):
        if cur_sum < 0:
            cur_sum = nums[i]
        else:
            cur_sum += nums[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum
