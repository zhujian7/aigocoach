import pytest
from palindrome_partition import partition



def sort_2d(lst):
    if lst is None:
        return None
    return sorted([sorted(sub) for sub in lst])


@pytest.mark.parametrize("name, s, want", [
    ("example aab", "aab", [["a", "a", "b"], ["aa", "b"]]),
    ("single char", "a", [["a"]]),
    ("all same chars", "aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
    ("no palindrome partitions beyond singles", "abc", [["a", "b", "c"]]),
    ("full palindrome", "aba", [["a", "b", "a"], ["aba"]]),
    ("two chars same", "bb", [["b", "b"], ["bb"]]),
])
def test_partition(name, s, want):
    result = partition(s)
    assert sort_2d(result) == sort_2d(want), f"{name}: got {result}, want {want}"
