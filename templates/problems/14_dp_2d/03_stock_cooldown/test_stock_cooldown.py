import pytest
from stock_cooldown import max_profit_cooldown


@pytest.mark.parametrize("name, prices, want", [
    ("example 1", [1, 2, 3, 0, 2], 3),
    ("single day", [1], 0),
    ("decreasing prices", [5, 4, 3, 2, 1], 0),
    ("two days profit", [1, 2], 1),
    ("two days no profit", [2, 1], 0),
    ("alternating", [1, 4, 2, 7], 6),
])
def test_max_profit_cooldown(name, prices, want):
    result = max_profit_cooldown(prices)
    assert result == want, f"{name}: got {result}, want {want}"
