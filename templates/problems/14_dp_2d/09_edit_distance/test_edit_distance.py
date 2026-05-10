import pytest
from edit_distance import min_distance


@pytest.mark.parametrize("name, word1, word2, want", [
    ("horse to ros", "horse", "ros", 3),
    ("intention to execution", "intention", "execution", 5),
    ("empty to abc", "", "abc", 3),
    ("abc to empty", "abc", "", 3),
    ("both empty", "", "", 0),
    ("same strings", "abc", "abc", 0),
    ("single char different", "a", "b", 1),
])
def test_min_distance(name, word1, word2, want):
    result = min_distance(word1, word2)
    assert result == want, f"{name}: got {result}, want {want}"
