import pytest
from n_queens import solve_n_queens


def sort_2d(lst):
    if lst is None:
        return None
    return sorted([sorted(sub) for sub in lst])


# Expected solution counts for n-queens
_EXPECTED_COUNTS = {5: 10, 6: 4, 8: 92}


@pytest.mark.parametrize("name, n, wantBoards", [
    ("n=1", 1, [["Q"]]),
    ("n=2 no solution", 2, []),
    ("n=3 no solution", 3, []),
    ("n=4", 4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
    ("n=5", 5, None),
    ("n=6", 6, None),
    ("n=8", 8, None),
])
def test_solve_n_queens(name, n, wantBoards):
    result = solve_n_queens(n)
    if wantBoards is None:
        expected_count = _EXPECTED_COUNTS[n]
        assert len(result) == expected_count, (
            f"{name}: got {len(result)} solutions, want {expected_count}"
        )
    else:
        assert sort_2d(result) == sort_2d(wantBoards), (
            f"{name}: got {result}, want {wantBoards}"
        )
