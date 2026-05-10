from typing import Optional
from tree_node import TreeNode


def solve_is_valid_bst(root: Optional[TreeNode]) -> bool:
    return validate_bst(root, float('-inf'), float('inf'))


def validate_bst(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
    if node is None:
        return True
    if node.val <= min_val or node.val >= max_val:
        return False
    return validate_bst(node.left, min_val, node.val) and validate_bst(node.right, node.val, max_val)
