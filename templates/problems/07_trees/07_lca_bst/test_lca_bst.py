import pytest
from tree_node import build_tree, TreeNode
from lca_bst import lowest_common_ancestor


def find_node(root, val):
    """Find a TreeNode with the given value in the tree."""
    if root is None:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)


@pytest.mark.parametrize("name, vals, pVal, qVal, wantV", [
    ("example 1", [6, 2, 8, 0, 4, 7, 9, -101, -101, 3, 5], 2, 8, 6),
    ("example 2", [6, 2, 8, 0, 4, 7, 9, -101, -101, 3, 5], 2, 4, 2),
    ("root is lca", [2, 1, 3], 1, 3, 2),
    ("same node", [2, 1, 3], 1, 1, 1),
    ("right subtree", [6, 2, 8, 0, 4, 7, 9], 7, 9, 8),
    ("deep nodes", [6, 2, 8, 0, 4, 7, 9, -101, -101, 3, 5], 3, 5, 4),
])
def test_lowest_common_ancestor(name, vals, pVal, qVal, wantV):
    root = build_tree(vals)
    p = find_node(root, pVal)
    q = find_node(root, qVal)
    got = lowest_common_ancestor(root, p, q)
    assert got is not None and got.val == wantV, (
        f"{name}: got {got.val if got else None}, want {wantV}"
    )
