import pytest
from reverse_integer import reverse


@pytest.mark.parametrize("name, x, expected", [
    ("positive", 123, 321),
    ("negative", -123, -321),
    ("trailing zero", 120, 21),
    ("zero", 0, 0),
    ("single digit", 5, 5),
    ("overflow positive", 1534236469, 0),
    ("overflow negative", -2147483648, 0),
])
def test_reverse(name, x, expected):
    result = reverse(x)
    assert result == expected, f"{name}: got {result}, want {expected}"
