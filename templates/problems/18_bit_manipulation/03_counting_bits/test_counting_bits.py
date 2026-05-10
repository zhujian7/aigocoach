import pytest
from counting_bits import count_bits


@pytest.mark.parametrize("name, n, expected", [
    ("n=2", 2, [0, 1, 1]),
    ("n=5", 5, [0, 1, 1, 2, 1, 2]),
    ("n=0", 0, [0]),
    ("n=1", 1, [0, 1]),
    ("n=8", 8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
    ("n=3", 3, [0, 1, 1, 2]),
])
def test_count_bits(name, n, expected):
    result = count_bits(n)
    assert result == expected, f"{name}: got {result}, want {expected}"
