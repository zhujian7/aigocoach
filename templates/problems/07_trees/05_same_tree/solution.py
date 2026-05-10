from typing import Optional
from tree_node import TreeNode


def solve_is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None or p.val != q.val:
        return False
    return solve_is_same_tree(p.left, q.left) and solve_is_same_tree(p.right, q.right)
