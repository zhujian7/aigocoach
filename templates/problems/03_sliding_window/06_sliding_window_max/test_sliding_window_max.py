import pytest
from sliding_window_max import max_sliding_window


@pytest.mark.parametrize("name, nums, k, expected", [
    ("basic case", [1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ("k equals array length", [1, 3, 2], 3, [3]),
    ("k equals 1", [1, -1, 3], 1, [1, -1, 3]),
    ("single element", [5], 1, [5]),
    ("decreasing sequence", [7, 6, 5, 4, 3], 2, [7, 6, 5, 4]),
    ("increasing sequence", [1, 2, 3, 4, 5], 2, [2, 3, 4, 5]),
    ("all same values", [4, 4, 4, 4], 2, [4, 4, 4]),
])
def test_max_sliding_window(name, nums, k, expected):
    result = max_sliding_window(nums, k)
    assert result == expected, f"{name}: got {result}, want {expected}"
