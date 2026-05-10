import pytest
from best_time_stock import max_profit


@pytest.mark.parametrize("name, prices, expected", [
    ("basic profit", [7, 1, 5, 3, 6, 4], 5),
    ("no profit possible", [7, 6, 4, 3, 1], 0),
    ("single day", [5], 0),
    ("two days profit", [1, 2], 1),
    ("two days no profit", [2, 1], 0),
    ("buy at start sell at end", [1, 2, 3, 4, 5], 4),
    ("all same price", [3, 3, 3, 3], 0),
])
def test_max_profit(name, prices, expected):
    result = max_profit(prices)
    assert result == expected, f"{name}: got {result}, want {expected}"
