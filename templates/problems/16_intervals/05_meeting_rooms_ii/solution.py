from typing import List


def solve_min_meeting_rooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    starts = sorted(iv[0] for iv in intervals)
    ends = sorted(iv[1] for iv in intervals)
    rooms = 0
    max_rooms = 0
    s = 0
    e = 0
    while s < len(starts):
        if starts[s] < ends[e]:
            rooms += 1
            s += 1
        else:
            rooms -= 1
            e += 1
        if rooms > max_rooms:
            max_rooms = rooms
    return max_rooms
