import pytest
from palindromic_substrings import count_substrings


@pytest.mark.parametrize("name, s, want", [
    ("example abc", "abc", 3),
    ("example aaa", "aaa", 6),
    ("single char", "a", 1),
    ("two same chars", "aa", 3),
    ("two different chars", "ab", 2),
    ("racecar", "racecar", 10),
])
def test_count_substrings(name, s, want):
    result = count_substrings(s)
    assert result == want, f"{name}: got {result}, want {want}"
