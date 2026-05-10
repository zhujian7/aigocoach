from collections import defaultdict
from typing import List


def solve_find_itinerary(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    for src, dst in tickets:
        graph[src].append(dst)
    for src in graph:
        graph[src].sort()

    result = []

    def dfs(airport: str) -> None:
        while graph[airport]:
            nxt = graph[airport].pop(0)
            dfs(nxt)
        result.append(airport)

    dfs("JFK")
    return result[::-1]
