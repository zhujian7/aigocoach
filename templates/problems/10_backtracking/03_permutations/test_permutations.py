import pytest
from permutations import permute



def sort_2d(lst):
    if lst is None:
        return None
    return sorted([sorted(sub) for sub in lst])


@pytest.mark.parametrize("name, nums, want", [
    ("three elements", [1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ("single element", [1], [[1]]),
    ("two elements", [0, 1], [[0, 1], [1, 0]]),
    ("negative numbers", [-1, 0, 1], [[-1, 0, 1], [-1, 1, 0], [0, -1, 1], [0, 1, -1], [1, -1, 0], [1, 0, -1]]),
    ("four elements count", [1, 2, 3, 4], None),
])
def test_permute(name, nums, want):
    result = permute(nums)
    if want is None:
        # count-only check: 4! = 24
        assert len(result) == 24, f"{name}: got {len(result)} permutations, want 24"
    else:
        assert sort_2d(result) == sort_2d(want), f"{name}: got {result}, want {want}"
