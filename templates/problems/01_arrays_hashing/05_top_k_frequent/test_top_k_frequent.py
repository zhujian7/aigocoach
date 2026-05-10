import pytest
from top_k_frequent import top_k_frequent


@pytest.mark.parametrize("name, nums, k, want", [
    ("basic case", [1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ("single element", [1], 1, [1]),
    ("all same frequency k equals length", [1, 2, 3], 3, [1, 2, 3]),
    ("negative numbers", [-1, -1, -2, -2, -2, -3], 1, [-2]),
    ("k equals 1 with clear winner", [4, 4, 4, 1, 2, 3], 1, [4]),
    ("two elements", [1, 2], 2, [1, 2]),
])
def test_top_k_frequent(name, nums, k, want):
    result = top_k_frequent(nums, k)
    assert sorted(result) == sorted(want), f"{name}: got {result}, want {want}"
