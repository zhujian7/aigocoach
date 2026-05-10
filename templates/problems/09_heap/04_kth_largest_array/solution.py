import heapq
from typing import List


def solve_find_kth_largest(nums: List[int], k: int) -> int:
    min_heap: List[int] = []
    for n in nums:
        heapq.heappush(min_heap, n)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
