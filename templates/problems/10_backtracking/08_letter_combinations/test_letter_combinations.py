import pytest
from letter_combinations import letter_combinations


@pytest.mark.parametrize("name, digits, want", [
    ("example 23", "23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("empty string", "", []),
    ("single digit 2", "2", ["a", "b", "c"]),
    ("digit 7 with four letters", "7", ["p", "q", "r", "s"]),
    ("digit 9 with four letters", "9", ["w", "x", "y", "z"]),
    ("three digits", "234", ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]),
])
def test_letter_combinations(name, digits, want):
    result = letter_combinations(digits)
    assert sorted(result) == sorted(want), f"{name}: got {result}, want {want}"
