import pytest
from valid_paren_string import check_valid_string


@pytest.mark.parametrize("name, s, expected", [
    ("simple valid", "()", True),
    ("star as empty", "(*)", True),
    ("star as paren", "(*))", True),
    ("empty string", "", True),
    ("only stars", "***", True),
    ("unmatched open", "((", False),
    ("unmatched close", "))", False),
    ("star as open", "*(", False),
])
def test_check_valid_string(name, s, expected):
    result = check_valid_string(s)
    assert result == expected, f"{name}: got {result}, want {expected}"
