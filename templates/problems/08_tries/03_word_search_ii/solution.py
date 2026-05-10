from typing import List


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.word: str = ""


def solve_find_words(board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    for w in words:
        node = root
        for c in w:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = w

    rows, cols = len(board), len(board[0])
    result: List[str] = []

    def dfs(r: int, c: int, node: TrieNode) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "#":
            return
        ch = board[r][c]
        nxt = node.children.get(ch)
        if nxt is None:
            return
        if nxt.word:
            result.append(nxt.word)
            nxt.word = ""
        board[r][c] = "#"
        dfs(r + 1, c, nxt)
        dfs(r - 1, c, nxt)
        dfs(r, c + 1, nxt)
        dfs(r, c - 1, nxt)
        board[r][c] = ch

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    return result
