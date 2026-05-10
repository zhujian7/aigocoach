import pytest
from rotate_image import rotate


@pytest.mark.parametrize("name, matrix, expected", [
    ("3x3", [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ("4x4", [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]], [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
    ("1x1", [[1]], [[1]]),
    ("2x2", [[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    ("all same", [[1, 1], [1, 1]], [[1, 1], [1, 1]]),
])
def test_rotate(name, matrix, expected):
    rotate(matrix)
    assert matrix == expected, f"{name}: got {matrix}, want {expected}"
