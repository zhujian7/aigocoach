import pytest
from valid_palindrome import is_palindrome


@pytest.mark.parametrize("name, s, expected", [
    ("alphanumeric palindrome with spaces and punctuation", "A man, a plan, a canal: Panama", True),
    ("not a palindrome", "race a car", False),
    ("empty string is palindrome", " ", True),
    ("single character", "a", True),
    ("mixed case palindrome", "Aa", True),
    ("digits in palindrome", "0P", False),
])
def test_is_palindrome(name, s, expected):
    result = is_palindrome(s)
    assert result == expected, f"{name}: got {result}, want {expected}"
