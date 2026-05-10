import pytest
from coin_change import coin_change


@pytest.mark.parametrize("name, coins, amount, want", [
    ("example 1", [1, 2, 5], 11, 3),
    ("impossible", [2], 3, -1),
    ("zero amount", [1], 0, 0),
    ("single coin exact", [1], 1, 1),
    ("single coin multiple", [1], 5, 5),
    ("large coins small amount", [5, 10], 3, -1),
    ("multiple denominations", [1, 5, 10, 25], 30, 2),
])
def test_coin_change(name, coins, amount, want):
    result = coin_change(coins, amount)
    assert result == want, f"{name}: got {result}, want {want}"
