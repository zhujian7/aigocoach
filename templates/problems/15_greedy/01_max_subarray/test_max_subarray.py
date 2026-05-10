import pytest
from max_subarray import max_sub_array


@pytest.mark.parametrize("name, nums, expected", [
    ("mixed positive and negative", [-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ("single element positive", [1], 1),
    ("single element negative", [-1], -1),
    ("all negative", [-2, -3, -1, -5], -1),
    ("all positive", [1, 2, 3, 4], 10),
    ("two elements", [-1, 2], 2),
    ("negative then positive", [-2, -1, 3, 4, -1, 2], 8),
])
def test_max_sub_array(name, nums, expected):
    result = max_sub_array(nums)
    assert result == expected, f"{name}: got {result}, want {expected}"
