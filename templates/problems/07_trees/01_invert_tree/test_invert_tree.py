import pytest
from tree_node import build_tree, tree_to_list
from invert_tree import invert_tree


@pytest.mark.parametrize("name, vals, want", [
    ("example 1", [4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ("example 2", [2, 1, 3], [2, 3, 1]),
    ("empty tree", [], []),
    ("single node", [1], [1]),
    ("left only", [1, 2], [1, -101, 2]),
    ("right only", [1, -101, 2], [1, 2]),
])
def test_invert_tree(name, vals, want):
    root = build_tree(vals)
    got = tree_to_list(invert_tree(root))
    assert got == want, f"{name}: got {got}, want {want}"
