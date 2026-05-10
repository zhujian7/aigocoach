import pytest
from meeting_rooms_ii import min_meeting_rooms


@pytest.mark.parametrize("name, intervals, expected", [
    ("two rooms", [[0, 30], [5, 10], [15, 20]], 2),
    ("one room", [[7, 10], [2, 4]], 1),
    ("all overlap", [[1, 5], [2, 6], [3, 7]], 3),
    ("single meeting", [[1, 10]], 1),
    ("sequential", [[0, 5], [5, 10], [10, 15]], 1),
    ("nested", [[1, 10], [2, 5], [6, 9]], 2),
    ("empty", [], 0),
])
def test_min_meeting_rooms(name, intervals, expected):
    result = min_meeting_rooms(intervals)
    assert result == expected, f"{name}: got {result}, want {expected}"
