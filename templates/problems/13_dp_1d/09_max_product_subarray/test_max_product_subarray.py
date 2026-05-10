import pytest
from max_product_subarray import max_product


@pytest.mark.parametrize("name, nums, want", [
    ("example 1", [2, 3, -2, 4], 6),
    ("example 2", [-2, 0, -1], 0),
    ("single negative", [-2], -2),
    ("two negatives", [-2, -3], 6),
    ("contains zero", [-2, 3, -4], 24),
    ("all positive", [1, 2, 3, 4], 24),
    ("single element", [5], 5),
])
def test_max_product(name, nums, want):
    result = max_product(nums)
    assert result == want, f"{name}: got {result}, want {want}"
