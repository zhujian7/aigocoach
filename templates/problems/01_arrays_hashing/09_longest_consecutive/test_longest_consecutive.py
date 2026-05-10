import pytest
from longest_consecutive import longest_consecutive


@pytest.mark.parametrize("name, nums, want", [
    ("basic case", [100, 4, 200, 1, 3, 2], 4),
    ("longer sequence", [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ("empty array", [], 0),
    ("single element", [1], 1),
    ("no consecutive", [10, 20, 30], 1),
    ("duplicates in sequence", [1, 2, 2, 3, 3, 4], 4),
    ("negative numbers", [-3, -2, -1, 0, 1], 5),
    ("all same elements", [5, 5, 5, 5], 1),
])
def test_longest_consecutive(name, nums, want):
    result = longest_consecutive(nums)
    assert result == want, f"{name}: got {result}, want {want}"
