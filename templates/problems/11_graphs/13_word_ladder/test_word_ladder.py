import pytest
from word_ladder import ladder_length


@pytest.mark.parametrize("name, beginWord, endWord, wordList, want", [
    ("standard transformation", "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
    ("no valid transformation", "hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ("one step", "hot", "dot", ["dot"], 2),
    ("same begin and end", "hit", "hit", ["hit"], 0),
    ("end word not in list", "abc", "xyz", ["abc", "xbc"], 0),
    ("longer path", "a", "c", ["a", "b", "c"], 2),
    ("two letter words", "ab", "cd", ["ad", "cb", "cd"], 3),
])
def test_ladder_length(name, beginWord, endWord, wordList, want):
    result = ladder_length(beginWord, endWord, wordList)
    assert result == want, f"{name}: got {result}, want {want}"
