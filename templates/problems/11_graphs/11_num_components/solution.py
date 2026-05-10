from typing import List


def count_components(n: int, edges: List[List[int]]) -> int:
    parent = list(range(n))
    rank = [0] * n
    components = n

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for a, b in edges:
        px, py = find(a), find(b)
        if px != py:
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            components -= 1

    return components
