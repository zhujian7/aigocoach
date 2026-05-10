import pytest
from largest_rect_histogram import largest_rectangle_area


@pytest.mark.parametrize("name, heights, want", [
    ("example 1", [2, 1, 5, 6, 2, 3], 10),
    ("single bar", [5], 5),
    ("increasing", [1, 2, 3, 4, 5], 9),
    ("decreasing", [5, 4, 3, 2, 1], 9),
    ("all same", [3, 3, 3, 3], 12),
    ("two bars", [2, 4], 4),
    ("valley", [6, 2, 5, 4, 5, 1, 6], 12),
    ("empty", [], 0),
])
def test_largest_rectangle_area(name, heights, want):
    result = largest_rectangle_area(heights)
    assert result == want, f"{name}: got {result}, want {want}"
