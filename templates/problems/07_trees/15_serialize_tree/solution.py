from typing import List, Optional
from tree_node import TreeNode


def solve_serialize(root: Optional[TreeNode]) -> str:
    parts: List[str] = []

    def preorder(node: Optional[TreeNode]) -> None:
        if node is None:
            parts.append("N,")
            return
        parts.append(str(node.val) + ",")
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return "".join(parts)


def solve_deserialize(data: str) -> Optional[TreeNode]:
    tokens = data.split(",")
    idx = [0]

    def build() -> Optional[TreeNode]:
        if idx[0] >= len(tokens) or tokens[idx[0]] == "N" or tokens[idx[0]] == "":
            idx[0] += 1
            return None
        val = int(tokens[idx[0]])
        idx[0] += 1
        node = TreeNode(val)
        node.left = build()
        node.right = build()
        return node

    return build()
