import pytest
from task_scheduler import least_interval


@pytest.mark.parametrize("name, tasks, n, want", [
    ("example 1", ["A", "A", "A", "B", "B", "B"], 2, 8),
    ("no cooldown", ["A", "A", "A", "B", "B", "B"], 0, 6),
    ("example 3", ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
    ("single task", ["A"], 5, 1),
    ("all different tasks", ["A", "B", "C", "D"], 3, 4),
    ("two tasks with cooldown 1", ["A", "A", "B", "B"], 1, 4),
])
def test_least_interval(name, tasks, n, want):
    result = least_interval(tasks, n)
    assert result == want, f"{name}: got {result}, want {want}"
