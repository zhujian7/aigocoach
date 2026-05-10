import pytest
from merge_intervals import merge


@pytest.mark.parametrize("name, intervals, expected", [
    ("overlapping", [[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ("touching", [[1, 4], [4, 5]], [[1, 5]]),
    ("no overlap", [[1, 2], [4, 5]], [[1, 2], [4, 5]]),
    ("single interval", [[1, 5]], [[1, 5]]),
    ("all merge", [[1, 4], [2, 5], [3, 6]], [[1, 6]]),
    ("unsorted input", [[3, 4], [1, 2], [5, 6]], [[1, 2], [3, 4], [5, 6]]),
    ("contained interval", [[1, 10], [3, 5]], [[1, 10]]),
])
def test_merge(name, intervals, expected):
    result = merge(intervals)
    assert result == expected, f"{name}: got {result}, want {expected}"
