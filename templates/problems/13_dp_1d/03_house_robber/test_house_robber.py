import pytest
from house_robber import rob


@pytest.mark.parametrize("name, nums, want", [
    ("example 1", [1, 2, 3, 1], 4),
    ("example 2", [2, 7, 9, 3, 1], 12),
    ("single house", [5], 5),
    ("two houses pick larger", [1, 2], 2),
    ("all same values", [3, 3, 3, 3], 6),
    ("empty", [], 0),
    ("large values alternating", [100, 1, 100, 1, 100], 300),
])
def test_rob(name, nums, want):
    result = rob(nums)
    assert result == want, f"{name}: got {result}, want {want}"
