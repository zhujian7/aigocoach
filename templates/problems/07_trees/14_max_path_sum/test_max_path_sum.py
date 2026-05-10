import pytest
from tree_node import build_tree
from max_path_sum import max_path_sum


@pytest.mark.parametrize("name, vals, want", [
    ("example 1", [1, 2, 3], 6),
    ("example 2", [-10, 9, 20, -101, -101, 15, 7], 42),
    ("single node", [1], 1),
    ("single negative", [-3], -3),
    ("all negative", [-1, -2, -3], -1),
    ("mixed", [5, 4, 8, 11, -101, 13, 4, 7, 2, -101, -101, -101, 1], 48),
])
def test_max_path_sum(name, vals, want):
    root = build_tree(vals)
    got = max_path_sum(root)
    assert got == want, f"{name}: got {got}, want {want}"
