import pytest
from tree_node import build_tree
from diameter import diameter_of_binary_tree


@pytest.mark.parametrize("name, vals, want", [
    ("example 1", [1, 2, 3, 4, 5], 3),
    ("example 2", [1, 2], 1),
    ("single node", [1], 0),
    ("empty tree", [], 0),
    ("left skewed", [1, 2, -101, 3, -101, 4], 3),
    ("wide tree", [1, 2, 3, 4, 5, 6, 7], 4),
])
def test_diameter_of_binary_tree(name, vals, want):
    root = build_tree(vals)
    got = diameter_of_binary_tree(root)
    assert got == want, f"{name}: got {got}, want {want}"
