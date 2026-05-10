import pytest
from daily_temperatures import daily_temperatures


@pytest.mark.parametrize("name, temperatures, want", [
    ("typical case", [73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ("decreasing", [30, 20, 10], [0, 0, 0]),
    ("increasing", [10, 20, 30], [1, 1, 0]),
    ("single element", [50], [0]),
    ("all same", [70, 70, 70, 70], [0, 0, 0, 0]),
    ("two elements warmer", [30, 60], [1, 0]),
    ("two elements cooler", [60, 30], [0, 0]),
])
def test_daily_temperatures(name, temperatures, want):
    result = daily_temperatures(temperatures)
    assert result == want, f"{name}: got {result}, want {want}"
