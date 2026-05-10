import pytest
from valid_parentheses import is_valid


@pytest.mark.parametrize("name, s, want", [
    ("empty string", "", True),
    ("single pair parens", "()", True),
    ("multiple types", "()[]{}", True),
    ("nested", "{[]}", True),
    ("mismatched", "(]", False),
    ("unmatched open", "([", False),
    ("complex valid", "({[()]})", True),
    ("single char", "(", False),
    ("unmatched close", "]", False),
    ("leading close", "]()", False),
])
def test_is_valid(name, s, want):
    result = is_valid(s)
    assert result == want, f"{name}: got {result}, want {want}"
