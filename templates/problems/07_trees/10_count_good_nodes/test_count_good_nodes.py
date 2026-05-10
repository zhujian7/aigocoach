import pytest
from tree_node import build_tree
from count_good_nodes import good_nodes


@pytest.mark.parametrize("name, vals, want", [
    ("example 1", [3, 1, 4, 3, -101, 1, 5], 4),
    ("example 2", [3, 3, -101, 4, 2], 3),
    ("single node", [1], 1),
    ("all same", [1, 1, 1, 1, 1], 5),
    ("decreasing", [5, 3, 4, 1, 2, -101, 3], 1),
    ("increasing left", [1, 2, -101, 3], 3),
])
def test_good_nodes(name, vals, want):
    root = build_tree(vals)
    got = good_nodes(root)
    assert got == want, f"{name}: got {got}, want {want}"
