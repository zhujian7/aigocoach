import pytest
from hand_of_straights import is_n_straight_hand


@pytest.mark.parametrize("name, hand, groupSize, expected", [
    ("example true", [1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True),
    ("example false", [1, 2, 3, 4, 5], 4, False),
    ("single group", [1, 2, 3], 3, True),
    ("group size 1", [5, 3, 1], 1, True),
    ("not divisible", [1, 2, 3, 4], 3, False),
    ("duplicates needed", [1, 1, 2, 2, 3, 3], 3, True),
    ("gap in sequence", [1, 2, 4, 5, 6, 7], 3, False),
])
def test_is_n_straight_hand(name, hand, groupSize, expected):
    result = is_n_straight_hand(hand, groupSize)
    assert result == expected, f"{name}: got {result}, want {expected}"
