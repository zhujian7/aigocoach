import pytest
from house_robber_ii import rob_ii


@pytest.mark.parametrize("name, nums, want", [
    ("example 1", [2, 3, 2], 3),
    ("example 2", [1, 2, 3, 1], 4),
    ("single house", [5], 5),
    ("two houses", [1, 2], 2),
    ("example 3", [1, 2, 3], 3),
    ("four houses", [1, 3, 1, 3, 100], 103),
    ("all same", [4, 4, 4, 4, 4], 8),
])
def test_rob_ii(name, nums, want):
    result = rob_ii(nums)
    assert result == want, f"{name}: got {result}, want {want}"
