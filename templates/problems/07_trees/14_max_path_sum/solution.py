from typing import Optional
from tree_node import TreeNode


def solve_max_path_sum(root: Optional[TreeNode]) -> int:
    result = float('-inf')

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal result
        if node is None:
            return 0
        left = dfs(node.left)
        if left < 0:
            left = 0
        right = dfs(node.right)
        if right < 0:
            right = 0
        path_sum = node.val + left + right
        if path_sum > result:
            result = path_sum
        if left > right:
            return node.val + left
        return node.val + right

    dfs(root)
    return result
