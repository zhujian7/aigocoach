import pytest
from min_cost_stairs import min_cost_climbing_stairs


@pytest.mark.parametrize("name, cost, want", [
    ("example 1", [10, 15, 20], 15),
    ("example 2", [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ("two steps equal cost", [5, 5], 5),
    ("two steps different cost", [1, 100], 1),
    ("increasing cost", [1, 2, 3, 4, 5], 6),
    ("all zeros", [0, 0, 0, 0], 0),
])
def test_min_cost_climbing_stairs(name, cost, want):
    result = min_cost_climbing_stairs(cost)
    assert result == want, f"{name}: got {result}, want {want}"
