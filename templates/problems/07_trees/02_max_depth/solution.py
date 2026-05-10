from typing import Optional
from tree_node import TreeNode


def solve_max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    left = solve_max_depth(root.left)
    right = solve_max_depth(root.right)
    if left > right:
        return left + 1
    return right + 1
