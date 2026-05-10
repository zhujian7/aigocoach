import pytest
from longest_increasing_path import longest_increasing_path


@pytest.mark.parametrize("name, matrix, want", [
    ("example 1", [[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
    ("example 2", [[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
    ("single cell", [[1]], 1),
    ("single row", [[1, 2, 3, 4]], 4),
    ("single column", [[1], [2], [3]], 3),
    ("all same values", [[5, 5], [5, 5]], 1),
])
def test_longest_increasing_path(name, matrix, want):
    result = longest_increasing_path(matrix)
    assert result == want, f"{name}: got {result}, want {want}"
