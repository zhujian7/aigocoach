from typing import List, Optional
from collections import deque
from tree_node import TreeNode


def solve_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        size = len(queue)
        level = []
        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(level)
    return result
