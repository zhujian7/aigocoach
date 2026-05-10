from typing import Optional
from tree_node import TreeNode


def solve_is_balanced(root: Optional[TreeNode]) -> bool:
    return height(root) != -1


def height(node: Optional[TreeNode]) -> int:
    if node is None:
        return 0
    left = height(node.left)
    if left == -1:
        return -1
    right = height(node.right)
    if right == -1:
        return -1
    diff = left - right
    if diff < -1 or diff > 1:
        return -1
    if left > right:
        return left + 1
    return right + 1
