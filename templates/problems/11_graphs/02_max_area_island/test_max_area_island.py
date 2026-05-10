import pytest
from max_area_island import max_area_of_island


@pytest.mark.parametrize("name, grid, want", [
    ("mixed islands", [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]], 6),
    ("all water", [[0, 0, 0], [0, 0, 0]], 0),
    ("single cell island", [[0, 1, 0], [0, 0, 0]], 1),
    ("entire grid is one island", [[1, 1], [1, 1]], 4),
    ("L-shaped island", [[1, 0], [1, 0], [1, 1]], 4),
    ("two separate islands", [[1, 0, 1, 1], [0, 0, 1, 1]], 4),
])
def test_max_area_of_island(name, grid, want):
    result = max_area_of_island(grid)
    assert result == want, f"{name}: got {result}, want {want}"
