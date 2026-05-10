import pytest
from coin_change_ii import change


@pytest.mark.parametrize("name, amount, coins, want", [
    ("example 1", 5, [1, 2, 5], 4),
    ("example 2", 3, [2], 0),
    ("zero amount", 0, [1, 2], 1),
    ("single coin", 10, [10], 1),
    ("single penny", 5, [1], 1),
    ("two coins", 4, [1, 2], 3),
])
def test_change(name, amount, coins, want):
    result = change(amount, coins)
    assert result == want, f"{name}: got {result}, want {want}"
