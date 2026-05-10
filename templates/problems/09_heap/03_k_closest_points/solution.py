import heapq
from typing import List


def solve_k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    max_heap: List[tuple[int, List[int]]] = []
    for p in points:
        dist = p[0] * p[0] + p[1] * p[1]
        heapq.heappush(max_heap, (-dist, p))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return [item[1] for item in max_heap]
