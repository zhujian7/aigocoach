from typing import List


def solve_longest_consecutive(nums: List[int]) -> int:
    num_set = set(nums)
    best = 0

    for n in num_set:
        if n - 1 in num_set:
            continue
        length = 1
        while n + length in num_set:
            length += 1
        if length > best:
            best = length
    return best
