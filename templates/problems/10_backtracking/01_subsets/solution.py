from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(start: int, current: List[int]) -> None:
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
