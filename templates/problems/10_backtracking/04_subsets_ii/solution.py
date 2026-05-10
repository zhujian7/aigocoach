from typing import List


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    def backtrack(start: int, current: List[int]) -> None:
        result.append(current[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
