from typing import List


def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    result = []

    def backtrack(start: int, remain: int, current: List[int]) -> None:
        if remain == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            current.append(candidates[i])
            backtrack(i + 1, remain - candidates[i], current)
            current.pop()

    backtrack(0, target, [])
    return result
