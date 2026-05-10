import heapq
from collections import deque


def solve_least_interval(tasks: str, n: int) -> int:
    freq = [0] * 26
    for t in tasks:
        freq[ord(t) - ord("A")] += 1
    max_heap: list[int] = []
    for f in freq:
        if f > 0:
            heapq.heappush(max_heap, -f)

    queue: deque[tuple[int, int]] = deque()
    time = 0

    while max_heap or queue:
        time += 1
        if max_heap:
            f = -heapq.heappop(max_heap) - 1
            if f > 0:
                queue.append((f, time + n))
        if queue and queue[0][1] == time:
            remain, _ = queue.popleft()
            heapq.heappush(max_heap, -remain)
    return time
