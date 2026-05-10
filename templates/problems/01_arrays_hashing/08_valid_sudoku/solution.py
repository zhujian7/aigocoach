from typing import List


def solve_is_valid_sudoku(board: List[List[str]]) -> bool:
    rows = [[False] * 9 for _ in range(9)]
    cols = [[False] * 9 for _ in range(9)]
    boxes = [[False] * 9 for _ in range(9)]

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            d = ord(board[r][c]) - ord('1')
            box = (r // 3) * 3 + c // 3

            if rows[r][d] or cols[c][d] or boxes[box][d]:
                return False
            rows[r][d] = True
            cols[c][d] = True
            boxes[box][d] = True
    return True
