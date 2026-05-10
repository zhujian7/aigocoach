from typing import List


def solve_trap(height: List[int]) -> int:
    if not height:
        return 0
    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]
    water = 0

    while l < r:
        if left_max < right_max:
            l += 1
            if height[l] > left_max:
                left_max = height[l]
            else:
                water += left_max - height[l]
        else:
            r -= 1
            if height[r] > right_max:
                right_max = height[r]
            else:
                water += right_max - height[r]
    return water
