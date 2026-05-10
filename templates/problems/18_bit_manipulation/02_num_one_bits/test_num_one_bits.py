import pytest
from num_one_bits import hamming_weight


@pytest.mark.parametrize("name, n, expected", [
    ("three ones", 0b00000000000000000000000000001011, 3),
    ("one bit", 0b00000000000000000000000010000000, 1),
    ("all ones 32bit", 0b11111111111111111111111111111101, 31),
    ("zero", 0, 0),
    ("power of two", 16, 1),
    ("all ones", 0xFFFFFFFF, 32),
])
def test_hamming_weight(name, n, expected):
    result = hamming_weight(n)
    assert result == expected, f"{name}: got {result}, want {expected}"
