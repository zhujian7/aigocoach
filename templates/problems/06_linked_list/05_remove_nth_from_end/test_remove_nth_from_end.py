import pytest
from list_node import build_list, list_to_array
from remove_nth_from_end import remove_nth_from_end


@pytest.mark.parametrize("name, vals, n, want", [
    ("remove last", [1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
    ("remove first", [1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
    ("remove middle", [1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
    ("single element", [1], 1, None),
    ("two elements remove last", [1, 2], 1, [1]),
    ("two elements remove first", [1, 2], 2, [2]),
])
def test_remove_nth_from_end(name, vals, n, want):
    head = build_list(vals)
    got = list_to_array(remove_nth_from_end(head, n))
    assert got == want, f"{name}: got {got}, want {want}"
