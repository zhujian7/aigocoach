import pytest
from happy_number import is_happy


@pytest.mark.parametrize("name, n, expected", [
    ("happy 19", 19, True),
    ("happy 1", 1, True),
    ("not happy 2", 2, False),
    ("happy 7", 7, True),
    ("not happy 4", 4, False),
    ("happy 100", 100, True),
    ("not happy 20", 20, False),
])
def test_is_happy(name, n, expected):
    result = is_happy(n)
    assert result == expected, f"{name}: got {result}, want {expected}"
