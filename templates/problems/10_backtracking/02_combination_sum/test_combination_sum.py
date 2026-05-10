import pytest
from combination_sum import combination_sum



def sort_2d(lst):
    if lst is None:
        return None
    return sorted([sorted(sub) for sub in lst])


@pytest.mark.parametrize("name, candidates, target, want", [
    ("example 1", [2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
    ("example 2", [2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ("no combination", [2], 1, []),
    ("single candidate equals target", [1], 1, [[1]]),
    ("single candidate repeated", [1], 3, [[1, 1, 1]]),
    ("multiple solutions", [2, 3, 7], 9, [[2, 7], [2, 2, 2, 3], [3, 3, 3]]),
])
def test_combination_sum(name, candidates, target, want):
    result = combination_sum(candidates, target)
    assert sort_2d(result) == sort_2d(want), f"{name}: got {result}, want {want}"
