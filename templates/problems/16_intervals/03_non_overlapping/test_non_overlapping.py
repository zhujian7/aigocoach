import pytest
from non_overlapping import erase_overlap_intervals


@pytest.mark.parametrize("name, intervals, expected", [
    ("one removal", [[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ("no removal", [[1, 2], [2, 3]], 0),
    ("all overlap", [[1, 2], [1, 2], [1, 2]], 2),
    ("single interval", [[1, 5]], 0),
    ("nested intervals", [[1, 10], [2, 3], [4, 5]], 1),
    ("chain overlap", [[1, 3], [2, 4], [3, 5]], 1),
])
def test_erase_overlap_intervals(name, intervals, expected):
    result = erase_overlap_intervals(intervals)
    assert result == expected, f"{name}: got {result}, want {expected}"
