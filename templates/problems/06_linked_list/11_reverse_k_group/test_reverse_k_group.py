import pytest
from list_node import build_list, list_to_array
from reverse_k_group import reverse_k_group


@pytest.mark.parametrize("name, vals, k, want", [
    ("nil list", None, 2, None),
    ("k equals 1", [1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
    ("k equals 2", [1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
    ("k equals 3", [1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ("exact groups", [1, 2, 3, 4], 2, [2, 1, 4, 3]),
    ("k equals length", [1, 2, 3], 3, [3, 2, 1]),
    ("k greater than length", [1, 2], 3, [1, 2]),
    ("single element", [1], 1, [1]),
])
def test_reverse_k_group(name, vals, k, want):
    head = build_list(vals)
    got = list_to_array(reverse_k_group(head, k))
    assert got == want, f"{name}: got {got}, want {want}"
