from typing import List
import heapq


def solve_min_interval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    intervals.sort(key=lambda x: x[0])
    sorted_q = sorted(enumerate(queries), key=lambda x: x[1])
    result = [-1] * len(queries)
    heap = []
    j = 0
    for idx, val in sorted_q:
        while j < len(intervals) and intervals[j][0] <= val:
            size = intervals[j][1] - intervals[j][0] + 1
            heapq.heappush(heap, (size, intervals[j][1]))
            j += 1
        while heap and heap[0][1] < val:
            heapq.heappop(heap)
        if heap:
            result[idx] = heap[0][0]
    return result
