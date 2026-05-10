import pytest
from find_min_rotated import find_min


@pytest.mark.parametrize("name, nums, want", [
    ("rotated", [3, 4, 5, 1, 2], 1),
    ("rotated once", [4, 5, 6, 7, 0, 1, 2], 0),
    ("not rotated", [11, 13, 15, 17], 11),
    ("single element", [1], 1),
    ("two elements rotated", [2, 1], 1),
    ("two elements sorted", [1, 2], 1),
    ("min at end", [2, 3, 4, 5, 1], 1),
    ("min at start", [1, 2, 3, 4, 5], 1),
])
def test_find_min(name, nums, want):
    result = find_min(nums)
    assert result == want, f"{name}: got {result}, want {want}"
