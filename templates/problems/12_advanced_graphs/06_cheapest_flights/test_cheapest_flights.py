import pytest
from cheapest_flights import find_cheapest_price


@pytest.mark.parametrize("name, n, flights, src, dst, k, want", [
    ("standard case", 4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1, 700),
    ("direct flight", 3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
    ("cheaper with stop", 3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
    ("no route", 3, [[0, 1, 100]], 0, 2, 1, -1),
    ("not enough stops", 4, [[0, 1, 100], [1, 2, 100], [2, 3, 100]], 0, 3, 1, -1),
    ("same src and dst", 2, [[0, 1, 100]], 0, 0, 0, 0),
    ("two stops allowed", 4, [[0, 1, 100], [1, 2, 100], [2, 3, 100]], 0, 3, 2, 300),
])
def test_find_cheapest_price(name, n, flights, src, dst, k, want):
    result = find_cheapest_price(n, flights, src, dst, k)
    assert result == want, f"{name}: got {result}, want {want}"
