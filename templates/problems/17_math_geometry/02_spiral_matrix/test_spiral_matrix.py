import pytest
from spiral_matrix import spiral_order


@pytest.mark.parametrize("name, matrix, expected", [
    ("3x3", [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ("3x4", [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ("1x1", [[1]], [1]),
    ("1 row", [[1, 2, 3]], [1, 2, 3]),
    ("1 column", [[1], [2], [3]], [1, 2, 3]),
    ("2x2", [[1, 2], [3, 4]], [1, 2, 4, 3]),
])
def test_spiral_order(name, matrix, expected):
    result = spiral_order(matrix)
    assert result == expected, f"{name}: got {result}, want {expected}"
