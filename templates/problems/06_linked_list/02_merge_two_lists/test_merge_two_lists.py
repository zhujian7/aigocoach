import pytest
from list_node import build_list, list_to_array
from merge_two_lists import merge_two_lists


@pytest.mark.parametrize("name, list1, list2, want", [
    ("both nil", None, None, None),
    ("first nil", None, [1, 2, 3], [1, 2, 3]),
    ("second nil", [1, 2, 3], None, [1, 2, 3]),
    ("interleaved", [1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    ("one before other", [1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ("duplicates", [1, 1, 3], [1, 2, 4], [1, 1, 1, 2, 3, 4]),
    ("single elements", [5], [1], [1, 5]),
])
def test_merge_two_lists(name, list1, list2, want):
    l1 = build_list(list1)
    l2 = build_list(list2)
    got = list_to_array(merge_two_lists(l1, l2))
    assert got == want, f"{name}: got {got}, want {want}"
