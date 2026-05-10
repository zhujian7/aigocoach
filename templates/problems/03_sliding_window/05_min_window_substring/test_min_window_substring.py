import pytest
from min_window_substring import min_window


@pytest.mark.parametrize("name, s, t_str, expected", [
    ("basic case", "ADOBECODEBANC", "ABC", "BANC"),
    ("exact match", "a", "a", "a"),
    ("no valid window", "a", "aa", ""),
    ("t not in s", "abc", "z", ""),
    ("entire string is window", "abc", "abc", "abc"),
    ("duplicate chars in t", "aaabbc", "aab", "aab"),
    ("empty s", "", "a", ""),
])
def test_min_window(name, s, t_str, expected):
    result = min_window(s, t_str)
    assert result == expected, f"{name}: got {result}, want {expected}"
