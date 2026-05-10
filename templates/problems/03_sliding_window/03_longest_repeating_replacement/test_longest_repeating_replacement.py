import pytest
from longest_repeating_replacement import character_replacement


@pytest.mark.parametrize("name, s, k, expected", [
    ("basic case", "ABAB", 2, 4),
    ("replace one", "AABABBA", 1, 4),
    ("no replacement needed", "AAAA", 0, 4),
    ("single character", "A", 0, 1),
    ("k equals string length", "ABCD", 4, 4),
    ("alternating with k=0", "ABABAB", 0, 1),
])
def test_character_replacement(name, s, k, expected):
    result = character_replacement(s, k)
    assert result == expected, f"{name}: got {result}, want {expected}"
