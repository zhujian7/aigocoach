import pytest
from kth_largest_array import find_kth_largest


@pytest.mark.parametrize("name, nums, k, want", [
    ("example 1", [3, 2, 1, 5, 6, 4], 2, 5),
    ("example 2", [3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ("single element", [1], 1, 1),
    ("k equals length", [5, 3, 1], 3, 1),
    ("all same elements", [7, 7, 7, 7], 2, 7),
    ("negative numbers", [-1, -2, -3, -4], 1, -1),
    ("mixed positive and negative", [-1, 2, 0], 2, 0),
])
def test_find_kth_largest(name, nums, k, want):
    result = find_kth_largest(nums, k)
    assert result == want, f"{name}: got {result}, want {want}"
