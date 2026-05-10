import pytest
from search_rotated import search_rotated


@pytest.mark.parametrize("name, nums, target, want", [
    ("found in left half", [4, 5, 6, 7, 0, 1, 2], 0, 4),
    ("found in right half", [4, 5, 6, 7, 0, 1, 2], 5, 1),
    ("not found", [4, 5, 6, 7, 0, 1, 2], 3, -1),
    ("single element found", [1], 1, 0),
    ("single element not found", [1], 0, -1),
    ("not rotated found", [1, 2, 3, 4, 5], 3, 2),
    ("two elements", [3, 1], 1, 1),
    ("target at pivot", [6, 7, 1, 2, 3, 4, 5], 1, 2),
])
def test_search_rotated(name, nums, target, want):
    result = search_rotated(nums, target)
    assert result == want, f"{name}: got {result}, want {want}"
