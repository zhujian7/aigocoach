import pytest
from longest_common_sub import longest_common_subsequence


@pytest.mark.parametrize("name, text1, text2, want", [
    ("example 1", "abcde", "ace", 3),
    ("example 2", "abc", "abc", 3),
    ("no common", "abc", "def", 0),
    ("one char vs longer", "a", "abc", 1),
    ("single char match", "a", "a", 1),
    ("single char no match", "a", "b", 0),
    ("longer example", "oxcpqrsvwf", "shmtulqrypy", 2),
])
def test_longest_common_subsequence(name, text1, text2, want):
    result = longest_common_subsequence(text1, text2)
    assert result == want, f"{name}: got {result}, want {want}"
