import pytest
from surrounded_regions import solve


@pytest.mark.parametrize("name, board, want", [
    ("standard case", [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]], [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]),
    ("single cell X", [["X"]], [["X"]]),
    ("single cell O", [["O"]], [["O"]]),
    ("all O on border", [["O", "O"], ["O", "O"]], [["O", "O"], ["O", "O"]]),
    ("O connected to border", [["X", "O", "X"], ["X", "O", "X"], ["X", "X", "X"]], [["X", "O", "X"], ["X", "O", "X"], ["X", "X", "X"]]),
    ("surrounded O in center", [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]], [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]),
])
def test_solve(name, board, want):
    solve(board)
    assert board == want, f"{name}: got {board}, want {want}"
