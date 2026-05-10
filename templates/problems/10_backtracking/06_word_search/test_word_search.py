import pytest
from word_search import exist


@pytest.mark.parametrize("name, board, word, want", [
    ("word exists", [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
    ("word exists path SEE", [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
    ("word does not exist", [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
    ("single cell match", [["A"]], "A", True),
    ("single cell no match", [["A"]], "B", False),
    ("word longer than board cells", [["A", "B"], ["C", "D"]], "ABCDA", False),
    ("snake path", [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]], "ABCFEDGHI", True),
])
def test_exist(name, board, word, want):
    result = exist(board, word)
    assert result == want, f"{name}: got {result}, want {want}"
