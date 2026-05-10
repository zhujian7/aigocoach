import pytest
from partition_equal_subset import can_partition


@pytest.mark.parametrize("name, nums, want", [
    ("example can partition", [1, 5, 11, 5], True),
    ("example cannot partition", [1, 2, 3, 5], False),
    ("two equal elements", [1, 1], True),
    ("single element", [1], False),
    ("odd total sum", [1, 2, 4], False),
    ("larger example", [1, 2, 3, 4, 5, 6, 7], True),
    ("all zeros", [0, 0, 0, 0], True),
])
def test_can_partition(name, nums, want):
    result = can_partition(nums)
    assert result == want, f"{name}: got {result}, want {want}"
