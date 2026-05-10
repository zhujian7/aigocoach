import pytest
from contains_duplicate import contains_duplicate


@pytest.mark.parametrize("name, nums, want", [
    ("has duplicates", [1, 2, 3, 1], True),
    ("no duplicates", [1, 2, 3, 4], False),
    ("empty slice", [], False),
    ("single element", [1], False),
    ("all same elements", [5, 5, 5, 5], True),
    ("duplicates at end", [1, 2, 3, 4, 5, 5], True),
    ("negative numbers with duplicates", [-1, -2, -3, -1], True),
])
def test_contains_duplicate(name, nums, want):
    result = contains_duplicate(nums)
    assert result == want, f"{name}: got {result}, want {want}"
