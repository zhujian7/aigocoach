import pytest
from trapping_rain_water import trap


@pytest.mark.parametrize("name, height, expected", [
    ("basic case", [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ("v shape", [4, 2, 0, 3, 2, 5], 9),
    ("no water", [1, 2, 3, 4, 5], 0),
    ("empty input", [], 0),
    ("single bar", [5], 0),
    ("two bars", [3, 1], 0),
    ("flat surface", [3, 3, 3, 3], 0),
])
def test_trap(name, height, expected):
    result = trap(height)
    assert result == expected, f"{name}: got {result}, want {expected}"
