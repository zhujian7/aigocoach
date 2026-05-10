import pytest
from reverse_bits import reverse_bits


@pytest.mark.parametrize("name, num, expected", [
    ("example 1", 0b00000010100101000001111010011100, 964176192),
    ("example 2", 0b11111111111111111111111111111101, 3221225471),
    ("zero", 0, 0),
    ("all ones", 0xFFFFFFFF, 0xFFFFFFFF),
    ("one", 1, 0x80000000),
    ("power of two", 0x80000000, 1),
])
def test_reverse_bits(name, num, expected):
    result = reverse_bits(num)
    assert result == expected, f"{name}: got {result}, want {expected}"
