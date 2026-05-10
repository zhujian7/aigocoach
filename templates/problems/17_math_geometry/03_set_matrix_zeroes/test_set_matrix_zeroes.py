import pytest
from set_matrix_zeroes import set_zeroes


@pytest.mark.parametrize("name, matrix, expected", [
    ("example 1", [[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    ("example 2", [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
    ("no zeros", [[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ("all zeros", [[0, 0], [0, 0]], [[0, 0], [0, 0]]),
    ("single element zero", [[0]], [[0]]),
    ("single element nonzero", [[5]], [[5]]),
    ("corner zero", [[0, 1], [1, 1]], [[0, 0], [0, 1]]),
])
def test_set_zeroes(name, matrix, expected):
    set_zeroes(matrix)
    assert matrix == expected, f"{name}: got {matrix}, want {expected}"
