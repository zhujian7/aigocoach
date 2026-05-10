import pytest
from gas_station import can_complete_circuit


@pytest.mark.parametrize("name, gas, cost, expected", [
    ("example 1", [1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ("no solution", [2, 3, 4], [3, 4, 3], -1),
    ("single station enough", [5], [3], 0),
    ("single station not enough", [2], [4], -1),
    ("start at index 0", [3, 1, 1], [1, 2, 2], 0),
    ("all equal", [1, 1, 1], [1, 1, 1], 0),
    ("start at last", [1, 1, 5], [2, 3, 1], 2),
])
def test_can_complete_circuit(name, gas, cost, expected):
    result = can_complete_circuit(gas, cost)
    assert result == expected, f"{name}: got {result}, want {expected}"
