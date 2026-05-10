import pytest
from merge_triplets import merge_triplets


@pytest.mark.parametrize("name, triplets, target, expected", [
    ("example true", [[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5], True),
    ("example false", [[3, 4, 5], [4, 5, 6]], [3, 2, 5], False),
    ("exact match single", [[2, 5, 3]], [2, 5, 3], True),
    ("no valid triplet", [[1, 1, 1]], [2, 2, 2], False),
    ("filter out exceeding", [[2, 5, 3], [10, 1, 1], [1, 7, 5]], [2, 7, 5], True),
    ("all exceed one dim", [[3, 1, 1], [3, 2, 2]], [2, 2, 2], False),
    ("multiple combos", [[1, 2, 3], [2, 1, 3], [2, 2, 1]], [2, 2, 3], True),
])
def test_merge_triplets(name, triplets, target, expected):
    result = merge_triplets(triplets, target)
    assert result == expected, f"{name}: got {result}, want {expected}"
