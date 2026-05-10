import pytest
from valid_anagram import is_anagram


@pytest.mark.parametrize("name, s, t, want", [
    ("valid anagram", "anagram", "nagaram", True),
    ("not anagram", "rat", "car", False),
    ("empty strings", "", "", True),
    ("different lengths", "ab", "abc", False),
    ("single characters same", "a", "a", True),
    ("single characters different", "a", "b", False),
    ("repeated characters", "aabb", "bbaa", True),
    ("same chars different frequency", "aaab", "aabb", False),
])
def test_is_anagram(name, s, t, want):
    result = is_anagram(s, t)
    assert result == want, f"{name}: got {result}, want {want}"
