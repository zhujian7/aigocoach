from typing import List


def solve_longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    memo = [[0] * n for _ in range(m)]
    result = 0
    for i in range(m):
        for j in range(n):
            result = max(result, _dfs(matrix, memo, i, j, m, n))
    return result


_dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def _dfs(matrix: List[List[int]], memo: List[List[int]], i: int, j: int, m: int, n: int) -> int:
    if memo[i][j] != 0:
        return memo[i][j]
    memo[i][j] = 1
    for di, dj in _dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
            memo[i][j] = max(memo[i][j], 1 + _dfs(matrix, memo, ni, nj, m, n))
    return memo[i][j]
