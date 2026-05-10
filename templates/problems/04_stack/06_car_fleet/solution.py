from typing import List


def solve_car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    n = len(position)
    if n == 0:
        return 0
    cars = sorted(zip(position, speed), reverse=True)
    fleets = 0
    last_time = 0.0
    for pos, spd in cars:
        time = (target - pos) / spd
        if time > last_time:
            fleets += 1
            last_time = time
    return fleets
