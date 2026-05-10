import pytest
from pow_x_n import my_pow


@pytest.mark.parametrize("name, x, n, expected", [
    ("positive exponent", 2.0, 10, 1024.0),
    ("negative exponent", 2.0, -2, 0.25),
    ("zero exponent", 5.0, 0, 1.0),
    ("exponent 1", 3.0, 1, 3.0),
    ("fractional base", 2.1, 3, 9.261),
    ("base 1", 1.0, 100, 1.0),
    ("base 0", 0.0, 5, 0.0),
])
def test_my_pow(name, x, n, expected):
    result = my_pow(x, n)
    assert abs(result - expected) < 1e-5, f"{name}: got {result}, want {expected}"
