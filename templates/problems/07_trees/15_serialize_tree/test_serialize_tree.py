import pytest
from tree_node import build_tree, tree_to_list
from serialize_tree import serialize, deserialize


@pytest.mark.parametrize("name,vals", [
    ("example 1", [1, 2, 3, -101, -101, 4, 5]),
    ("empty tree", []),
    ("single node", [1]),
    ("left only", [1, 2]),
    ("right only", [1, -101, 2]),
    ("full tree", [1, 2, 3, 4, 5, 6, 7]),
])
def test_serialize_deserialize(name, vals):
    root = build_tree(vals)
    want = tree_to_list(root)
    data = serialize(root)
    got = tree_to_list(deserialize(data))
    assert got == want, f"{name}: serialize/deserialize roundtrip = {got}, want {want}"
