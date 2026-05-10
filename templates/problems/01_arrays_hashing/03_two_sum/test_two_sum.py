import pytest
from two_sum import two_sum


@pytest.mark.parametrize("name, nums, target, want", [
    ("basic case", [2, 7, 11, 15], 9, [0, 1]),
    ("elements not adjacent", [3, 2, 4], 6, [1, 2]),
    ("same element value", [3, 3], 6, [0, 1]),
    ("negative numbers", [-1, -2, -3, -4, -5], -8, [2, 4]),
    ("mixed positive and negative", [-3, 4, 3, 90], 0, [0, 2]),
    ("large array target at end", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19, [8, 9]),
])
def test_two_sum(name, nums, target, want):
    result = two_sum(nums, target)
    assert sorted(result) == sorted(want), f"{name}: got {result}, want {want}"
