import pytest
from pacific_atlantic import pacific_atlantic



def sort_2d(lst):
    if lst is None:
        return None
    return sorted([sorted(sub) for sub in lst])


@pytest.mark.parametrize("name, heights, want", [
    ("standard grid", [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]], [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
    ("single cell", [[1]], [[0, 0]]),
    ("flat grid", [[1, 1], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 1]]),
    ("descending to corner", [[3, 2], [2, 1]], [[0, 0], [0, 1], [1, 0]]),
    ("single row", [[1, 2, 3]], [[0, 0], [0, 1], [0, 2]]),
    ("single column", [[3], [2], [1]], [[0, 0], [1, 0], [2, 0]]),
])
def test_pacific_atlantic(name, heights, want):
    result = pacific_atlantic(heights)
    assert sort_2d(result) == sort_2d(want), f"{name}: got {result}, want {want}"
