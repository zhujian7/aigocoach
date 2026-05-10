import pytest
from course_schedule_ii import find_order


def is_valid_topological_order(order, num_courses, prerequisites):
    """Check if order is a valid topological ordering."""
    if len(order) != num_courses:
        return False
    if set(order) != set(range(num_courses)):
        return False
    pos = {course: i for i, course in enumerate(order)}
    for course, prereq in prerequisites:
        if pos[prereq] >= pos[course]:
            return False
    return True


@pytest.mark.parametrize("name, numCourses, prerequisites, hasOrder", [
    ("two courses with dependency", 2, [[1, 0]], True),
    ("four courses", 4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),
    ("cycle returns empty", 2, [[1, 0], [0, 1]], False),
    ("single course", 1, [], True),
    ("no prerequisites", 3, [], True),
    ("three node cycle", 3, [[0, 1], [1, 2], [2, 0]], False),
])
def test_find_order(name, numCourses, prerequisites, hasOrder):
    result = find_order(numCourses, prerequisites)
    if hasOrder:
        assert is_valid_topological_order(result, numCourses, prerequisites), (
            f"{name}: got {result}, not a valid topological order"
        )
    else:
        assert result == [], f"{name}: got {result}, want []"
