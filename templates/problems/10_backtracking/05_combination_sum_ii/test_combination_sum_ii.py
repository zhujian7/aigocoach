import pytest
from combination_sum_ii import combination_sum2



def sort_2d(lst):
    if lst is None:
        return None
    return sorted([sorted(sub) for sub in lst])


@pytest.mark.parametrize("name, candidates, target, want", [
    ("example 1", [10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
    ("example 2", [2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
    ("no combination", [3, 5], 1, []),
    ("single element matches", [1], 1, [[1]]),
    ("all duplicates", [2, 2, 2], 4, [[2, 2]]),
    ("target zero", [1, 2, 3], 0, [[]]),
])
def test_combination_sum2(name, candidates, target, want):
    result = combination_sum2(candidates, target)
    assert sort_2d(result) == sort_2d(want), f"{name}: got {result}, want {want}"
