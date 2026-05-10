import pytest
from find_duplicate import find_duplicate


@pytest.mark.parametrize("name, nums, want", [
    ("simple", [1, 3, 4, 2, 2], 2),
    ("duplicate three", [3, 1, 3, 4, 2], 3),
    ("all same", [1, 1, 1, 1, 1], 1),
    ("two elements", [1, 1], 1),
    ("duplicate at end", [2, 5, 9, 6, 9, 3, 8, 9, 7, 1], 9),
    ("duplicate two", [3, 3, 3, 3, 3], 3),
])
def test_find_duplicate(name, nums, want):
    result = find_duplicate(nums)
    assert result == want, f"{name}: got {result}, want {want}"
