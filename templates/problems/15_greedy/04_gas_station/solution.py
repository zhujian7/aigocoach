from typing import List


def solve_can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    total_surplus = 0
    current_surplus = 0
    start = 0
    for i in range(len(gas)):
        total_surplus += gas[i] - cost[i]
        current_surplus += gas[i] - cost[i]
        if current_surplus < 0:
            start = i + 1
            current_surplus = 0
    if total_surplus < 0:
        return -1
    return start
