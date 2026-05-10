import pytest
from product_except_self import product_except_self


@pytest.mark.parametrize("name, nums, want", [
    ("basic case", [1, 2, 3, 4], [24, 12, 8, 6]),
    ("contains zero", [-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ("two elements", [2, 3], [3, 2]),
    ("all ones", [1, 1, 1, 1], [1, 1, 1, 1]),
    ("contains negative numbers", [-1, 2, -3, 4], [-24, 12, -8, 6]),
    ("two zeros", [0, 0, 1, 2], [0, 0, 0, 0]),
    ("large values", [10, 20, 30], [600, 300, 200]),
])
def test_product_except_self(name, nums, want):
    result = product_except_self(nums)
    assert result == want, f"{name}: got {result}, want {want}"
