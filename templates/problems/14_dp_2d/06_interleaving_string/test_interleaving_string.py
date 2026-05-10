import pytest
from interleaving_string import is_interleave


@pytest.mark.parametrize("name, s1, s2, s3, want", [
    ("example true", "aabcc", "dbbca", "aadbbcbcac", True),
    ("example false", "aabcc", "dbbca", "aadbbbaccc", False),
    ("both empty", "", "", "", True),
    ("s1 empty", "", "abc", "abc", True),
    ("s2 empty", "abc", "", "abc", True),
    ("length mismatch", "a", "b", "abc", False),
    ("single chars true", "a", "b", "ab", True),
])
def test_is_interleave(name, s1, s2, s3, want):
    result = is_interleave(s1, s2, s3)
    assert result == want, f"{name}: got {result}, want {want}"
