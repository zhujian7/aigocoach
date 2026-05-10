import pytest
from tree_node import build_tree
from balanced_tree import is_balanced


@pytest.mark.parametrize("name, vals, want", [
    ("balanced", [3, 9, 20, -101, -101, 15, 7], True),
    ("unbalanced", [1, 2, 2, 3, 3, -101, -101, 4, 4], False),
    ("empty tree", [], True),
    ("single node", [1], True),
    ("two levels balanced", [1, 2, 3], True),
    ("left heavy by one", [1, 2, -101, 3], False),
    ("deep unbalanced with right depth 0", [1, 2, -101, 3, -101, 4], False),
])
def test_is_balanced(name, vals, want):
    root = build_tree(vals)
    got = is_balanced(root)
    assert got == want, f"{name}: got {got}, want {want}"
