import pytest
from single_number import single_number


@pytest.mark.parametrize("name, nums, expected", [
    ("example 1", [2, 2, 1], 1),
    ("example 2", [4, 1, 2, 1, 2], 4),
    ("single element", [1], 1),
    ("negative numbers", [-1, -1, -2], -2),
    ("zero is single", [0, 1, 1], 0),
    ("larger array", [1, 3, 1, 2, 3], 2),
])
def test_single_number(name, nums, expected):
    result = single_number(nums)
    assert result == expected, f"{name}: got {result}, want {expected}"
