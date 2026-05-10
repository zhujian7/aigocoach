import pytest
from min_interval_query import min_interval


@pytest.mark.parametrize("name, intervals, queries, expected", [
    ("example 1", [[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5], [3, 3, 1, 4]),
    ("example 2", [[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22], [2, -1, 4, 6]),
    ("no intervals", [], [1, 2], [-1, -1]),
    ("query outside all", [[1, 3]], [5], [-1]),
    ("single point interval", [[5, 5]], [5], [1]),
    ("multiple covering", [[1, 10], [2, 5], [3, 4]], [3], [2]),
])
def test_min_interval(name, intervals, queries, expected):
    result = min_interval(intervals, queries)
    assert result == expected, f"{name}: got {result}, want {expected}"
