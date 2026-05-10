import pytest
from jump_game_ii import jump


@pytest.mark.parametrize("name, nums, expected", [
    ("example 1", [2, 3, 1, 1, 4], 2),
    ("example 2", [2, 3, 0, 1, 4], 2),
    ("single element", [0], 0),
    ("two elements", [1, 2], 1),
    ("already at end", [1], 0),
    ("linear jumps", [1, 1, 1, 1], 3),
    ("large first jump", [5, 1, 1, 1, 1, 1], 1),
])
def test_jump(name, nums, expected):
    result = jump(nums)
    assert result == expected, f"{name}: got {result}, want {expected}"
