from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []
    used = [False] * len(nums)

    def backtrack(current: List[int]) -> None:
        if len(current) == len(nums):
            result.append(current[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False

    backtrack([])
    return result
