import pytest
from tree_node import tree_to_list
from build_tree import build_tree_from_pre_in


@pytest.mark.parametrize("name, preorder, inorder, want", [
    ("example 1", [3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, -101, -101, 15, 7]),
    ("single node", [1], [1], [1]),
    ("left only", [1, 2], [2, 1], [1, 2]),
    ("right only", [1, 2], [1, 2], [1, -101, 2]),
    ("empty", [], [], []),
    ("three nodes", [1, 2, 3], [2, 1, 3], [1, 2, 3]),
])
def test_build_tree_from_pre_in(name, preorder, inorder, want):
    root = build_tree_from_pre_in(preorder, inorder)
    result = tree_to_list(root)
    assert result == want, f"{name}: got {result}, want {want}"
