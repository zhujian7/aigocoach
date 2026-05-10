from typing import Dict, List, Optional
from tree_node import TreeNode


def solve_build_tree_from_pre_in(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    in_map: Dict[int, int] = {}
    for i, v in enumerate(inorder):
        in_map[v] = i
    idx = [0]

    def build(lo: int, hi: int) -> Optional[TreeNode]:
        if lo > hi:
            return None
        root_val = preorder[idx[0]]
        idx[0] += 1
        node = TreeNode(root_val)
        mid = in_map[root_val]
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(inorder) - 1)
