import pytest
from meeting_rooms import can_attend_meetings


@pytest.mark.parametrize("name, intervals, expected", [
    ("overlapping", [[0, 30], [5, 10], [15, 20]], False),
    ("no overlap", [[7, 10], [2, 4]], True),
    ("empty", [], True),
    ("single meeting", [[1, 5]], True),
    ("touching boundaries", [[1, 5], [5, 10]], True),
    ("same time", [[1, 5], [1, 5]], False),
    ("sequential", [[0, 1], [1, 2], [2, 3]], True),
])
def test_can_attend_meetings(name, intervals, expected):
    result = can_attend_meetings(intervals)
    assert result == expected, f"{name}: got {result}, want {expected}"
