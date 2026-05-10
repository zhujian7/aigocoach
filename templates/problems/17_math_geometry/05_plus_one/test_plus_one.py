import pytest
from plus_one import plus_one


@pytest.mark.parametrize("name, digits, expected", [
    ("no carry", [1, 2, 3], [1, 2, 4]),
    ("single carry", [4, 3, 2, 9], [4, 3, 3, 0]),
    ("all nines", [9, 9, 9], [1, 0, 0, 0]),
    ("single digit", [0], [1]),
    ("single nine", [9], [1, 0]),
    ("large number", [8, 9, 9, 9], [9, 0, 0, 0]),
])
def test_plus_one(name, digits, expected):
    result = plus_one(digits)
    assert result == expected, f"{name}: got {result}, want {expected}"
