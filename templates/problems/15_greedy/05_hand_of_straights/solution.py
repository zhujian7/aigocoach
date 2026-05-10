from typing import List
from collections import Counter


def solve_is_n_straight_hand(hand: List[int], group_size: int) -> bool:
    if len(hand) % group_size != 0:
        return False
    freq = Counter(hand)
    hand.sort()
    for card in hand:
        if freq[card] == 0:
            continue
        for i in range(group_size):
            if freq[card + i] == 0:
                return False
            freq[card + i] -= 1
    return True
