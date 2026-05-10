import pytest
from three_sum import three_sum



def sort_2d(lst):
    if lst is None:
        return None
    return sorted([sorted(sub) for sub in lst])


@pytest.mark.parametrize("name, nums, expected", [
    ("basic case", [-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ("no triplets", [0, 1, 1], []),
    ("all zeros", [0, 0, 0], [[0, 0, 0]]),
    ("empty input", [], []),
    ("two elements only", [-1, 1], []),
    ("multiple triplets", [-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ("all positive", [1, 2, 3, 4, 5], []),
])
def test_three_sum(name, nums, expected):
    result = three_sum(nums)
    assert sort_2d(result) == sort_2d(expected), f"{name}: got {result}, want {expected}"
