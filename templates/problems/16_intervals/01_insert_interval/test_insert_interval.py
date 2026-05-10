import pytest
from insert_interval import insert


@pytest.mark.parametrize("name, intervals, newInterval, expected", [
    ("merge in middle", [[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ("merge multiple", [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ("empty intervals", [], [5, 7], [[5, 7]]),
    ("insert at beginning", [[3, 5], [6, 9]], [1, 2], [[1, 2], [3, 5], [6, 9]]),
    ("insert at end", [[1, 3], [6, 9]], [10, 12], [[1, 3], [6, 9], [10, 12]]),
    ("merge all", [[1, 3], [4, 6], [7, 9]], [0, 10], [[0, 10]]),
    ("no overlap", [[1, 2], [5, 6]], [3, 4], [[1, 2], [3, 4], [5, 6]]),
])
def test_insert(name, intervals, newInterval, expected):
    result = insert(intervals, newInterval)
    assert result == expected, f"{name}: got {result}, want {expected}"
