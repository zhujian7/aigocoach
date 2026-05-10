from typing import List


def solve_merge_triplets(triplets: List[List[int]], target: List[int]) -> bool:
    good = [False, False, False]
    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue
        for i in range(3):
            if t[i] == target[i]:
                good[i] = True
    return good[0] and good[1] and good[2]
