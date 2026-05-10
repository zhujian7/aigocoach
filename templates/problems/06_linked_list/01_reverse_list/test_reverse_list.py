import pytest
from list_node import build_list, list_to_array
from reverse_list import reverse_list


@pytest.mark.parametrize("name, vals, want", [
    ("nil list", None, None),
    ("single element", [1], [1]),
    ("two elements", [1, 2], [2, 1]),
    ("multiple elements", [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ("duplicates", [1, 1, 2, 2], [2, 2, 1, 1]),
    ("negative values", [-1, 0, 1], [1, 0, -1]),
])
def test_reverse_list(name, vals, want):
    head = build_list(vals)
    got = list_to_array(reverse_list(head))
    assert got == want, f"{name}: got {got}, want {want}"
