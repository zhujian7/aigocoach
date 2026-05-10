import pytest
from tree_node import build_tree
from validate_bst import is_valid_bst


@pytest.mark.parametrize("name, vals, want", [
    ("valid bst", [2, 1, 3], True),
    ("invalid bst", [5, 1, 4, -101, -101, 3, 6], False),
    ("single node", [1], True),
    ("empty tree", [], True),
    ("left equal", [2, 2, 3], False),
    ("valid larger", [5, 3, 7, 1, 4, 6, 8], True),
    ("invalid deep right", [5, 4, 6, -101, -101, 3, 7], False),
])
def test_is_valid_bst(name, vals, want):
    root = build_tree(vals)
    got = is_valid_bst(root)
    assert got == want, f"{name}: got {got}, want {want}"
