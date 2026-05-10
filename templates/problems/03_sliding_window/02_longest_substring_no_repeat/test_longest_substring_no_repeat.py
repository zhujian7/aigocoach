import pytest
from longest_substring_no_repeat import length_of_longest_substring


@pytest.mark.parametrize("name, s, expected", [
    ("basic case", "abcabcbb", 3),
    ("all same characters", "bbbbb", 1),
    ("mixed repeats", "pwwkew", 3),
    ("empty string", "", 0),
    ("single character", "a", 1),
    ("all unique", "abcdef", 6),
    ("spaces and special chars", "a b c", 3),
])
def test_length_of_longest_substring(name, s, expected):
    result = length_of_longest_substring(s)
    assert result == expected, f"{name}: got {result}, want {expected}"
