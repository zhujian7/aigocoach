import pytest
from container_most_water import max_area


@pytest.mark.parametrize("name, height, expected", [
    ("basic case", [1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ("two elements", [1, 1], 1),
    ("decreasing heights", [4, 3, 2, 1, 4], 16),
    ("equal heights", [5, 5, 5, 5], 15),
    ("one tall wall", [1, 2, 1], 2),
    ("large difference", [1, 1000, 1000, 1], 1000),
])
def test_max_area(name, height, expected):
    result = max_area(height)
    assert result == expected, f"{name}: got {result}, want {expected}"
