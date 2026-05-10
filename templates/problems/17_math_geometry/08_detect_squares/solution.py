from typing import List
from collections import defaultdict


class SolveDetectSquares:
    def __init__(self):
        self.point_count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.point_count[(point[0], point[1])] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point[0], point[1]
        total = 0
        for p in self.points:
            qx, qy = p[0], p[1]
            dx = qx - px
            dy = qy - py
            if abs(dx) != abs(dy) or dx == 0:
                continue
            total += (
                self.point_count[(px, qy)]
                * self.point_count[(qx, py)]
            )
        return total
