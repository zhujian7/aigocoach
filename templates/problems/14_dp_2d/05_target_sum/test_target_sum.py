import pytest
from target_sum import find_target_sum_ways


@pytest.mark.parametrize("name, nums, target, want", [
    ("example 1", [1, 1, 1, 1, 1], 3, 5),
    ("single element match", [1], 1, 1),
    ("single element negative", [1], -1, 1),
    ("impossible target", [1], 2, 0),
    ("two elements", [1, 2], 1, 1),
    ("all zeros", [0, 0, 0], 0, 8),
])
def test_find_target_sum_ways(name, nums, target, want):
    result = find_target_sum_ways(nums, target)
    assert result == want, f"{name}: got {result}, want {want}"
