from typing import Optional
from tree_node import TreeNode


def solve_is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    if root is None:
        return sub_root is None
    if same_tree(root, sub_root):
        return True
    return solve_is_subtree(root.left, sub_root) or solve_is_subtree(root.right, sub_root)


def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None or p.val != q.val:
        return False
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)
