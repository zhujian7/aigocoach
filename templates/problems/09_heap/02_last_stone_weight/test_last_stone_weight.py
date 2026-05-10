import pytest
from last_stone_weight import last_stone_weight


@pytest.mark.parametrize("name, stones, want", [
    ("example from problem", [2, 7, 4, 1, 8, 1], 1),
    ("single stone", [1], 1),
    ("two equal stones", [3, 3], 0),
    ("two different stones", [1, 5], 4),
    ("all same weight", [2, 2, 2, 2], 0),
    ("descending weights", [10, 5, 3, 1], 1),
    ("three stones", [3, 7, 2], 2),
])
def test_last_stone_weight(name, stones, want):
    result = last_stone_weight(stones)
    assert result == want, f"{name}: got {result}, want {want}"
