import pytest
from list_node import build_list, list_to_array
from reorder_list import reorder_list


@pytest.mark.parametrize("name, vals, want", [
    ("nil list", None, None),
    ("single element", [1], [1]),
    ("two elements", [1, 2], [1, 2]),
    ("three elements", [1, 2, 3], [1, 3, 2]),
    ("four elements", [1, 2, 3, 4], [1, 4, 2, 3]),
    ("five elements", [1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ("six elements", [1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
])
def test_reorder_list(name, vals, want):
    head = build_list(vals)
    got = list_to_array(reorder_list(head))
    assert got == want, f"{name}: got {got}, want {want}"
