from typing import List
from collections import deque


def walls_and_gates(rooms: List[List[int]]) -> None:
    if not rooms:
        return
    rows, cols = len(rooms), len(rooms[0])
    INF = 2147483647
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))
