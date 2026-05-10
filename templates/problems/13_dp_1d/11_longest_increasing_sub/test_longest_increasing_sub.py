import pytest
from longest_increasing_sub import length_of_lis


@pytest.mark.parametrize("name, nums, want", [
    ("example 1", [10, 9, 2, 5, 3, 7, 101, 18], 4),
    ("all increasing", [1, 2, 3, 4, 5], 5),
    ("all decreasing", [5, 4, 3, 2, 1], 1),
    ("single element", [7], 1),
    ("example 2", [0, 1, 0, 3, 2, 3], 4),
    ("duplicates", [7, 7, 7, 7, 7], 1),
])
def test_length_of_lis(name, nums, want):
    result = length_of_lis(nums)
    assert result == want, f"{name}: got {result}, want {want}"
