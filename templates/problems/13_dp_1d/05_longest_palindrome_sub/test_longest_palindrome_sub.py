import pytest
from longest_palindrome_sub import longest_palindrome


@pytest.mark.parametrize("name, s, want", [
    ("example babad", "babad", ["bab", "aba"]),
    ("example cbbd", "cbbd", ["bb"]),
    ("single character", "a", ["a"]),
    ("all same characters", "aaaa", ["aaaa"]),
    ("entire string is palindrome", "racecar", ["racecar"]),
    ("no repeats", "abcde", ["a", "b", "c", "d", "e"]),
    ("two characters same", "bb", ["bb"]),
])
def test_longest_palindrome(name, s, want):
    result = longest_palindrome(s)
    assert result in want, (
        f"{name}: got \"{result}\", want one of {want}"
    )
