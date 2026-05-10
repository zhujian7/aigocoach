import pytest
from search_2d_matrix import search_matrix


@pytest.mark.parametrize("name, matrix, target, want", [
    ("found in middle row", [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
    ("not found", [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ("found first element", [[1, 3, 5, 7], [10, 11, 16, 20]], 1, True),
    ("found last element", [[1, 3, 5, 7], [10, 11, 16, 20]], 20, True),
    ("single element found", [[1]], 1, True),
    ("single element not found", [[1]], 2, False),
    ("single row", [[1, 3, 5]], 3, True),
    ("single column", [[1], [3], [5]], 5, True),
])
def test_search_matrix(name, matrix, target, want):
    result = search_matrix(matrix, target)
    assert result == want, f"{name}: got {result}, want {want}"
