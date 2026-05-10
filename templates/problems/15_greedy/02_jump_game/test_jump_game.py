import pytest
from jump_game import can_jump


@pytest.mark.parametrize("name, nums, expected", [
    ("reachable", [2, 3, 1, 1, 4], True),
    ("not reachable", [3, 2, 1, 0, 4], False),
    ("single element", [0], True),
    ("two elements reachable", [1, 0], True),
    ("all zeros except first", [5, 0, 0, 0, 0], True),
    ("large first jump", [10, 0, 0, 0, 0, 0, 0, 0, 1], True),
    ("stuck at zero", [1, 0, 1], False),
])
def test_can_jump(name, nums, expected):
    result = can_jump(nums)
    assert result == expected, f"{name}: got {result}, want {expected}"
