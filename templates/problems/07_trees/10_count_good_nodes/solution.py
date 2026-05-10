from typing import Optional
from tree_node import TreeNode


def solve_good_nodes(root: Optional[TreeNode]) -> int:
    def dfs(node: Optional[TreeNode], max_so_far: int) -> int:
        if node is None:
            return 0
        count = 0
        if node.val >= max_so_far:
            count = 1
            max_so_far = node.val
        return count + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)

    return dfs(root, root.val)
