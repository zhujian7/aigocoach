from typing import List


def solve_find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    lo, hi = 0, m
    MIN_INT = -1000001
    MAX_INT = 1000001
    while lo <= hi:
        i = (lo + hi) // 2
        j = (m + n + 1) // 2 - i
        max_left_a = MIN_INT if i == 0 else nums1[i - 1]
        min_right_a = MAX_INT if i == m else nums1[i]
        max_left_b = MIN_INT if j == 0 else nums2[j - 1]
        min_right_b = MAX_INT if j == n else nums2[j]
        if max_left_a <= min_right_b and max_left_b <= min_right_a:
            if (m + n) % 2 == 1:
                return float(max(max_left_a, max_left_b))
            return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2.0
        elif max_left_a > min_right_b:
            hi = i - 1
        else:
            lo = i + 1
    return 0.0
