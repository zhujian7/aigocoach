import pytest
from subsets import subsets



def sort_2d(lst):
    if lst is None:
        return None
    return sorted([sorted(sub) for sub in lst])


@pytest.mark.parametrize("name, nums, want", [
    ("three elements", [1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
    ("single element", [0], [[], [0]]),
    ("two elements", [1, 2], [[], [1], [2], [1, 2]]),
    ("empty input", [], [[]]),
    ("negative numbers", [-1, 0], [[], [-1], [0], [-1, 0]]),
    ("five elements - slice sharing regression", [9, 0, 3, 5, 7], [[], [9], [0], [3], [5], [7], [9, 0], [9, 3], [9, 5], [9, 7], [0, 3], [0, 5], [0, 7], [3, 5], [3, 7], [5, 7], [9, 0, 3], [9, 0, 5], [9, 0, 7], [9, 3, 5], [9, 3, 7], [9, 5, 7], [0, 3, 5], [0, 3, 7], [0, 5, 7], [3, 5, 7], [9, 0, 3, 5], [9, 0, 3, 7], [9, 0, 5, 7], [9, 3, 5, 7], [0, 3, 5, 7], [9, 0, 3, 5, 7]]),
    ("four elements", [1, 2, 3, 4], [[], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]),
])
def test_subsets(name, nums, want):
    result = subsets(nums)
    assert sort_2d(result) == sort_2d(want), f"{name}: got {result}, want {want}"
