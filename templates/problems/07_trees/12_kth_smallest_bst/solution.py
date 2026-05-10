from typing import Optional
from tree_node import TreeNode


def solve_kth_smallest(root: Optional[TreeNode], k: int) -> int:
    count = 0
    result = 0

    def inorder(node: Optional[TreeNode]) -> None:
        nonlocal count, result
        if node is None or count >= k:
            return
        inorder(node.left)
        count += 1
        if count == k:
            result = node.val
            return
        inorder(node.right)

    inorder(root)
    return result
