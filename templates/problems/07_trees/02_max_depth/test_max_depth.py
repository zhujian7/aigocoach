import pytest
from tree_node import build_tree
from max_depth import max_depth


@pytest.mark.parametrize("name, vals, want", [
    ("example 1", [3, 9, 20, -101, -101, 15, 7], 3),
    ("example 2", [1, -101, 2], 2),
    ("empty tree", [], 0),
    ("single node", [1], 1),
    ("left skewed", [1, 2, -101, 3], 3),
    ("balanced depth 4", [1, 2, 3, 4, 5, 6, 7, 8], 4),
])
def test_max_depth(name, vals, want):
    root = build_tree(vals)
    got = max_depth(root)
    assert got == want, f"{name}: got {got}, want {want}"
