from typing import Optional
from tree_node import TreeNode


# Time: O(n), Space: O(h) where h is the height of the tree.
def solve_invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    solve_invert_tree(root.left)
    solve_invert_tree(root.right)
    return root
