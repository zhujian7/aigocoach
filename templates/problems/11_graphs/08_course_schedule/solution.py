from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 0=unvisited, 1=visiting, 2=visited
    state = [0] * num_courses

    def has_cycle(node: int) -> bool:
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False
        state[node] = 1
        for nxt in graph[node]:
            if has_cycle(nxt):
                return True
        state[node] = 2
        return False

    for i in range(num_courses):
        if has_cycle(i):
            return False
    return True
