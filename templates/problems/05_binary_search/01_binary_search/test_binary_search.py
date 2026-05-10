import pytest
from binary_search import search


@pytest.mark.parametrize("name, nums, target, want", [
    ("found middle", [-1, 0, 3, 5, 9, 12], 9, 4),
    ("found first", [-1, 0, 3, 5, 9, 12], -1, 0),
    ("found last", [-1, 0, 3, 5, 9, 12], 12, 5),
    ("not found", [-1, 0, 3, 5, 9, 12], 2, -1),
    ("single element found", [5], 5, 0),
    ("single element not found", [5], 3, -1),
    ("two elements", [1, 3], 3, 1),
    ("empty array", [], 1, -1),
])
def test_search(name, nums, target, want):
    result = search(nums, target)
    assert result == want, f"{name}: got {result}, want {want}"
