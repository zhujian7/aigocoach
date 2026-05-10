import pytest
from min_cost_connect import min_cost_connect_points


@pytest.mark.parametrize("name, points, want", [
    ("five points", [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
    ("three collinear points", [[3, 12], [-2, 5], [-4, 1]], 18),
    ("single point", [[0, 0]], 0),
    ("two points", [[0, 0], [1, 1]], 2),
    ("square corners", [[0, 0], [0, 1], [1, 0], [1, 1]], 3),
    ("negative coordinates", [[-1, -1], [-3, -3], [1, 1]], 8),
])
def test_min_cost_connect_points(name, points, want):
    result = min_cost_connect_points(points)
    assert result == want, f"{name}: got {result}, want {want}"
