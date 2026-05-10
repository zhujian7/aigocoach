import pytest
from course_schedule import can_finish


@pytest.mark.parametrize("name, numCourses, prerequisites, want", [
    ("simple chain", 2, [[1, 0]], True),
    ("cycle detected", 2, [[1, 0], [0, 1]], False),
    ("no prerequisites", 3, [], True),
    ("diamond dependency", 4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),
    ("three node cycle", 3, [[0, 1], [1, 2], [2, 0]], False),
    ("single course", 1, [], True),
    ("disconnected courses", 5, [[1, 0], [3, 2]], True),
])
def test_can_finish(name, numCourses, prerequisites, want):
    result = can_finish(numCourses, prerequisites)
    assert result == want, f"{name}: got {result}, want {want}"
