from typing import List


def solve_partition_labels(s: str) -> List[int]:
    last = {}
    for i, c in enumerate(s):
        last[c] = i
    result = []
    start = 0
    end = 0
    for i, c in enumerate(s):
        if last[c] > end:
            end = last[c]
        if i == end:
            result.append(end - start + 1)
            start = end + 1
    return result
