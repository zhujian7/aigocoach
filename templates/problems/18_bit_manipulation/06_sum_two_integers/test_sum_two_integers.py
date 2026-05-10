import pytest
from sum_two_integers import get_sum


@pytest.mark.parametrize("name, a, b, expected", [
    ("both positive", 1, 2, 3),
    ("positive and negative", 2, -1, 1),
    ("both negative", -1, -1, -2),
    ("zero and number", 0, 5, 5),
    ("both zero", 0, 0, 0),
    ("larger numbers", 100, 200, 300),
    ("negative result", -5, 3, -2),
])
def test_get_sum(name, a, b, expected):
    result = get_sum(a, b)
    assert result == expected, f"{name}: got {result}, want {expected}"
