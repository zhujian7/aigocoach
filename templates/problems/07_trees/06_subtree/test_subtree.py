import pytest
from tree_node import build_tree
from subtree import is_subtree


@pytest.mark.parametrize("name, root, subRoot, want", [
    ("is subtree", [3, 4, 5, 1, 2], [4, 1, 2], True),
    ("not subtree", [3, 4, 5, 1, 2, -101, -101, -101, -101, 0], [4, 1, 2], False),
    ("both single same", [1], [1], True),
    ("both single diff", [1], [2], False),
    ("sub is nil", [1, 2, 3], [], True),
    ("root equals sub", [1, 2, 3], [1, 2, 3], True),
])
def test_is_subtree(name, root, subRoot, want):
    root = build_tree(root)
    root2 = build_tree(subRoot)
    got = is_subtree(root, root2)
    assert got == want, f"{name}: got {got}, want {want}"
