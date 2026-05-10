import pytest
from list_node import build_list, list_to_array
from merge_k_lists import merge_k_lists


@pytest.mark.parametrize("name, lists_vals, want", [
    ("nil input", None, None),
    ("empty lists", [[], [], []], None),
    ("single list", [[1, 2, 3]], [1, 2, 3]),
    ("two lists", [[1, 4, 5], [1, 3, 4]], [1, 1, 3, 4, 4, 5]),
    ("three lists", [[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ("with empty list", [[1, 2], [], [3, 4]], [1, 2, 3, 4]),
    ("all single elements", [[5], [1], [3]], [1, 3, 5]),
    ("duplicates across lists", [[1, 1], [1, 1]], [1, 1, 1, 1]),
])
def test_merge_k_lists(name, lists_vals, want):
    if lists_vals is None:
        lists = None
    else:
        lists = [build_list(v) for v in lists_vals]
    got = list_to_array(merge_k_lists(lists))
    assert got == want, f"{name}: got {got}, want {want}"
