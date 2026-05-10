import pytest
from car_fleet import car_fleet


@pytest.mark.parametrize("name, target, position, speed, want", [
    ("example 1", 12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
    ("single car", 10, [3], [3], 1),
    ("all same speed", 10, [0, 2, 4], [2, 2, 2], 3),
    ("all merge", 10, [6, 8], [5, 2], 1),
    ("no cars", 10, [], [], 0),
    ("two separate fleets", 100, [0, 50], [1, 1], 2),
])
def test_car_fleet(name, target, position, speed, want):
    result = car_fleet(target, position, speed)
    assert result == want, f"{name}: got {result}, want {want}"
