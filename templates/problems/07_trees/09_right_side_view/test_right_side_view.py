import pytest
from tree_node import build_tree
from right_side_view import right_side_view


@pytest.mark.parametrize("name, vals, want", [
    ("example 1", [1, 2, 3, -101, 5, -101, 4], [1, 3, 4]),
    ("example 2", [1, -101, 3], [1, 3]),
    ("empty tree", [], []),
    ("single node", [1], [1]),
    ("left deeper", [1, 2, 3, 4], [1, 3, 4]),
    ("all left", [1, 2, -101, 3], [1, 2, 3]),
])
def test_right_side_view(name, vals, want):
    root = build_tree(vals)
    got = right_side_view(root)
    assert got == want, f"{name}: got {got}, want {want}"
