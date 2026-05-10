import pytest
from regex_matching import is_match


@pytest.mark.parametrize("name, s, p, want", [
    ("no match", "aa", "a", False),
    ("star matches multiple", "aa", "a*", True),
    ("dot star matches all", "ab", ".*", True),
    ("mixed pattern", "aab", "c*a*b", True),
    ("empty string empty pattern", "", "", True),
    ("empty string star pattern", "", "a*", True),
    ("complex pattern", "mississippi", "mis*is*ip*.", True),
    ("dot matches single", "ab", ".b", True),
])
def test_is_match(name, s, p, want):
    result = is_match(s, p)
    assert result == want, f"{name}: got {result}, want {want}"
