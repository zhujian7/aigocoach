import pytest
from distinct_subsequences import num_distinct


@pytest.mark.parametrize("name, s, tt, want", [
    ("example rabbbit", "rabbbit", "rabbit", 3),
    ("example babgbag", "babgbag", "bag", 5),
    ("no match", "abc", "def", 0),
    ("t longer than s", "ab", "abc", 0),
    ("equal strings", "abc", "abc", 1),
    ("empty t", "abc", "", 1),
    ("single char repeated", "aaa", "a", 3),
])
def test_num_distinct(name, s, tt, want):
    result = num_distinct(s, tt)
    assert result == want, f"{name}: got {result}, want {want}"
