import pytest
from tree_node import build_tree
from kth_smallest_bst import kth_smallest


@pytest.mark.parametrize("name, vals, k, want", [
    ("example 1", [3, 1, 4, -101, 2], 1, 1),
    ("example 2", [5, 3, 6, 2, 4, -101, -101, 1], 3, 3),
    ("single node k=1", [1], 1, 1),
    ("k equals size", [2, 1, 3], 3, 3),
    ("middle element", [3, 1, 4, -101, 2], 2, 2),
    ("large bst k=4", [5, 3, 7, 1, 4, 6, 8], 4, 5),
])
def test_kth_smallest(name, vals, k, want):
    root = build_tree(vals)
    got = kth_smallest(root, k)
    assert got == want, f"{name}: got {got}, want {want}"
