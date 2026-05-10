import heapq
from typing import List


def solve_min_cost_connect_points(points: List[List[int]]) -> int:
    n = len(points)
    if n <= 1:
        return 0

    visited = [False] * n
    heap = [(0, 0)]
    total_cost = 0
    count = 0

    while count < n:
        cost, to = heapq.heappop(heap)
        if visited[to]:
            continue
        visited[to] = True
        total_cost += cost
        count += 1

        for j in range(n):
            if not visited[j]:
                dist = abs(points[to][0] - points[j][0]) + abs(points[to][1] - points[j][1])
                heapq.heappush(heap, (dist, j))

    return total_cost
