import pytest
from decode_ways import num_decodings


@pytest.mark.parametrize("name, s, want", [
    ("example 12", "12", 2),
    ("example 226", "226", 3),
    ("leading zero", "06", 0),
    ("single digit", "1", 1),
    ("example 11106", "11106", 2),
    ("all ones", "1111", 5),
    ("example 10", "10", 1),
    ("example 27", "27", 1),
])
def test_num_decodings(name, s, want):
    result = num_decodings(s)
    assert result == want, f"{name}: got {result}, want {want}"
