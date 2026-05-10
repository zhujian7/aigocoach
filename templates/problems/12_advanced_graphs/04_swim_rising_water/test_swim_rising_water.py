import pytest
from swim_rising_water import swim_in_water


@pytest.mark.parametrize("name, grid, want", [
    ("2x2 grid", [[0, 2], [1, 3]], 3),
    ("5x5 grid", [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]], 16),
    ("single cell", [[0]], 0),
    ("3x3 grid", [[0, 1, 2], [5, 4, 3], [6, 7, 8]], 8),
    ("direct path best", [[0, 3, 5], [1, 4, 6], [2, 7, 8]], 8),
    ("2x2 easy", [[0, 1], [2, 3]], 3),
])
def test_swim_in_water(name, grid, want):
    result = swim_in_water(grid)
    assert result == want, f"{name}: got {result}, want {want}"
