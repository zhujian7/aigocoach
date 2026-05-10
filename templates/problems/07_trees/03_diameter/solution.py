from typing import Optional
from tree_node import TreeNode


def solve_diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    result = 0

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal result
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        if left + right > result:
            result = left + right
        if left > right:
            return left + 1
        return right + 1

    dfs(root)
    return result
