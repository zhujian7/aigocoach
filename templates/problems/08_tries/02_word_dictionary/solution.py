class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False


class SolveWordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._search_node(self.root, word, 0)

    def _search_node(self, node: TrieNode, word: str, i: int) -> bool:
        if i == len(word):
            return node.is_end
        c = word[i]
        if c == ".":
            for child in node.children.values():
                if self._search_node(child, word, i + 1):
                    return True
            return False
        child = node.children.get(c)
        if child is None:
            return False
        return self._search_node(child, word, i + 1)
