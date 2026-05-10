import pytest
from group_anagrams import group_anagrams



def sort_2d(lst):
    if lst is None:
        return None
    return sorted([sorted(sub) for sub in lst])


@pytest.mark.parametrize("name, strs, want", [
    ("mixed anagram groups", ["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    ("single empty string", [""], [[""]]),
    ("single non-empty string", ["a"], [["a"]]),
    ("no anagrams", ["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
    ("all anagrams", ["abc", "bca", "cab"], [["abc", "bca", "cab"]]),
    ("empty input", [], []),
    ("multiple empty strings", ["", ""], [["", ""]]),
])
def test_group_anagrams(name, strs, want):
    result = group_anagrams(strs)
    assert sort_2d(result) == sort_2d(want), f"{name}: got {result}, want {want}"
