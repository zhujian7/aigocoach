import pytest
from missing_number import missing_number


@pytest.mark.parametrize("name, nums, expected", [
    ("missing 2", [3, 0, 1], 2),
    ("missing 2 from 3", [0, 1], 2),
    ("missing 8", [9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ("missing 0", [1], 0),
    ("missing 1", [0], 1),
    ("single zero", [0, 2, 3], 1),
])
def test_missing_number(name, nums, expected):
    result = missing_number(nums)
    assert result == expected, f"{name}: got {result}, want {expected}"
