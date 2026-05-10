import pytest
from subsets_ii import subsets_with_dup



def sort_2d(lst):
    if lst is None:
        return None
    return sorted([sorted(sub) for sub in lst])


@pytest.mark.parametrize("name, nums, want", [
    ("example with duplicates", [1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
    ("single element", [0], [[], [0]]),
    ("all duplicates", [1, 1, 1], [[], [1], [1, 1], [1, 1, 1]]),
    ("no duplicates", [1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
    ("two pairs of duplicates", [1, 1, 2, 2], [[], [1], [2], [1, 1], [1, 2], [2, 2], [1, 1, 2], [1, 2, 2], [1, 1, 2, 2]]),
    ("unsorted input with duplicates", [2, 1, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
    ("empty input", [], [[]]),
])
def test_subsets_with_dup(name, nums, want):
    result = subsets_with_dup(nums)
    assert sort_2d(result) == sort_2d(want), f"{name}: got {result}, want {want}"
