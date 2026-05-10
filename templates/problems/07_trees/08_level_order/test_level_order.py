import pytest
from tree_node import build_tree
from level_order import level_order


@pytest.mark.parametrize("name, vals, want", [
    ("example 1", [3, 9, 20, -101, -101, 15, 7], [[3], [9, 20], [15, 7]]),
    ("example 2", [1], [[1]]),
    ("empty tree", [], []),
    ("two levels", [1, 2, 3], [[1], [2, 3]]),
    ("left only", [1, 2, -101, 3], [[1], [2], [3]]),
    ("full tree", [1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
])
def test_level_order(name, vals, want):
    root = build_tree(vals)
    got = level_order(root)
    assert got == want, f"{name}: got {got}, want {want}"
