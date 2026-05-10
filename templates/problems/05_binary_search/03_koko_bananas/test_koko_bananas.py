import pytest
from koko_bananas import min_eating_speed


@pytest.mark.parametrize("name, piles, h, want", [
    ("example 1", [3, 6, 7, 11], 8, 4),
    ("example 2", [30, 11, 23, 4, 20], 5, 30),
    ("example 3", [30, 11, 23, 4, 20], 6, 23),
    ("single pile exact", [10], 1, 10),
    ("single pile slow", [10], 10, 1),
    ("all ones", [1, 1, 1], 3, 1),
    ("large h", [3, 6, 7, 11], 100, 1),
])
def test_min_eating_speed(name, piles, h, want):
    result = min_eating_speed(piles, h)
    assert result == want, f"{name}: got {result}, want {want}"
