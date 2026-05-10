import pytest
from word_search_ii import find_words


@pytest.mark.parametrize("name, board, words, want", [
    ("example 1", [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"], ["eat", "oath"]),
    ("example 2", [["a", "b"], ["c", "d"]], ["abcb"], []),
    ("single cell match", [["a"]], ["a"], ["a"]),
    ("single cell no match", [["a"]], ["b"], []),
    ("multiple found", [["a", "b"], ["c", "d"]], ["ab", "ac", "abdc", "abcd", "dcba"], ["ab", "abdc", "ac"]),
    ("no words", [["a", "b"], ["c", "d"]], [], []),
])
def test_find_words(name, board, words, want):
    result = find_words(board, words)
    assert sorted(result) == sorted(want), f"{name}: got {result}, want {want}"
