import pytest
from permutation_in_string import check_inclusion


@pytest.mark.parametrize("name, s1, s2, expected", [
    ("permutation exists", "ab", "eidbaooo", True),
    ("no permutation", "ab", "eidboaoo", False),
    ("exact match", "abc", "bca", True),
    ("s1 longer than s2", "abcdef", "abc", False),
    ("single character match", "a", "a", True),
    ("single character no match", "a", "b", False),
    ("repeated characters", "aab", "ccccbaa", True),
])
def test_check_inclusion(name, s1, s2, expected):
    result = check_inclusion(s1, s2)
    assert result == expected, f"{name}: got {result}, want {expected}"
