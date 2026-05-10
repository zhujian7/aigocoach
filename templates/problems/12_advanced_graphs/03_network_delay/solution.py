import heapq
from collections import defaultdict
from typing import List


def solve_network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {}
    heap = [(0, k)]

    while heap:
        cost, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = cost
        for neighbor, weight in graph[node]:
            if neighbor not in dist:
                heapq.heappush(heap, (cost + weight, neighbor))

    if len(dist) != n:
        return -1
    return max(dist.values())
