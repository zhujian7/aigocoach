from typing import List


def solve_product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n

    result[0] = 1
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    suffix = 1
    for i in range(n - 2, -1, -1):
        suffix *= nums[i + 1]
        result[i] *= suffix

    return result
