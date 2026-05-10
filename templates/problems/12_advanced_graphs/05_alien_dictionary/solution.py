from collections import defaultdict, deque
from typing import List


def solve_alien_order(words: List[str]) -> str:
    graph = defaultdict(set)
    in_degree = {ch: 0 for word in words for ch in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        if len(w1) > len(w2) and w1[:len(w2)] == w2:
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    in_degree[c2] += 1
                break

    queue = deque(ch for ch in in_degree if in_degree[ch] == 0)
    result = []

    while queue:
        ch = queue.popleft()
        result.append(ch)
        for nxt in graph[ch]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(result) != len(in_degree):
        return ""
    return "".join(result)
