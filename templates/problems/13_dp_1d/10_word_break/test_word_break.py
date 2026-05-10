import pytest
from word_break import word_break


@pytest.mark.parametrize("name, s, wordDict, want", [
    ("example leetcode", "leetcode", ["leet", "code"], True),
    ("example applepenapple", "applepenapple", ["apple", "pen"], True),
    ("cannot break", "catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ("empty string", "", ["a"], True),
    ("single char match", "a", ["a"], True),
    ("single char no match", "b", ["a"], False),
    ("overlapping words", "cars", ["car", "ca", "rs"], True),
])
def test_word_break(name, s, wordDict, want):
    result = word_break(s, wordDict)
    assert result == want, f"{name}: got {result}, want {want}"
