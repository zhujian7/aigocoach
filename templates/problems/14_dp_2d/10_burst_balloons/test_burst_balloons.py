import pytest
from burst_balloons import max_coins


@pytest.mark.parametrize("name, nums, want", [
    ("example 1", [3, 1, 5, 8], 167),
    ("single balloon", [5], 5),
    ("two balloons", [1, 5], 10),
    ("example 2", [1, 5], 10),
    ("all ones", [1, 1, 1], 3),
    ("descending", [5, 4, 3, 2, 1], 110),
])
def test_max_coins(name, nums, want):
    result = max_coins(nums)
    assert result == want, f"{name}: got {result}, want {want}"
