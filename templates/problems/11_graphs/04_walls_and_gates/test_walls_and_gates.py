import pytest
from walls_and_gates import walls_and_gates

INF = 2147483647


@pytest.mark.parametrize("name,rooms,want", [
    (
        "standard grid",
        [
            [INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0, -1, INF, INF],
        ],
        [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ],
    ),
    ("single gate", [[0]], [[0]]),
    ("single wall", [[-1]], [[-1]]),
    ("no gates", [[INF, INF], [INF, INF]], [[INF, INF], [INF, INF]]),
    ("all gates", [[0, 0], [0, 0]], [[0, 0], [0, 0]]),
    (
        "gate in corner",
        [[0, INF], [INF, INF]],
        [[0, 1], [1, 2]],
    ),
])
def test_walls_and_gates(name, rooms, want):
    walls_and_gates(rooms)
    assert rooms == want, f"{name}: got {rooms}, want {want}"
