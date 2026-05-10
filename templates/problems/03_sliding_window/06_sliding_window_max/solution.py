from collections import deque
from typing import List


def solve_max_sliding_window(nums: List[int], k: int) -> List[int]:
    if not nums:
        return []

    dq = deque()
    result = []

    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
