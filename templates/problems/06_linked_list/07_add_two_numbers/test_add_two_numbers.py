import pytest
from list_node import build_list, list_to_array
from add_two_numbers import add_two_numbers


@pytest.mark.parametrize("name, l1, l2, want", [
    ("both zero", [0], [0], [0]),
    ("no carry", [2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ("with carry", [9, 9, 9], [1], [0, 0, 0, 1]),
    ("different lengths", [1, 8], [0], [1, 8]),
    ("single digits", [5], [5], [0, 1]),
    ("large carry chain", [9, 9, 9, 9], [1], [0, 0, 0, 0, 1]),
])
def test_add_two_numbers(name, l1, l2, want):
    l1 = build_list(l1)
    l2 = build_list(l2)
    got = list_to_array(add_two_numbers(l1, l2))
    assert got == want, f"{name}: got {got}, want {want}"
