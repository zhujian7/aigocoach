import pytest
from median_two_sorted import find_median_sorted_arrays


@pytest.mark.parametrize("name, nums1, nums2, want", [
    ("odd total", [1, 3], [2], 2.0),
    ("even total", [1, 2], [3, 4], 2.5),
    ("first empty", [], [1], 1.0),
    ("second empty", [2], [], 2.0),
    ("no overlap", [1, 2], [3, 4, 5], 3.0),
    ("interleaved", [1, 3, 5], [2, 4, 6], 3.5),
    ("single elements", [1], [2], 1.5),
    ("duplicates", [1, 1, 1], [1, 1, 1], 1.0),
])
def test_find_median_sorted_arrays(name, nums1, nums2, want):
    result = find_median_sorted_arrays(nums1, nums2)
    assert result == want, f"{name}: got {result}, want {want}"
