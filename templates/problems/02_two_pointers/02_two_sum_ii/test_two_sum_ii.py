import pytest
from two_sum_ii import two_sum_ii


@pytest.mark.parametrize("name, numbers, target, expected", [
    ("basic case", [2, 7, 11, 15], 9, [1, 2]),
    ("middle elements", [2, 3, 4], 6, [1, 3]),
    ("negative numbers", [-1, 0], -1, [1, 2]),
    ("larger array", [1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
    ("first and last", [1, 3, 5, 7], 8, [1, 4]),
    ("two elements", [5, 25], 30, [1, 2]),
])
def test_two_sum_ii(name, numbers, target, expected):
    result = two_sum_ii(numbers, target)
    assert result == expected, f"{name}: got {result}, want {expected}"
