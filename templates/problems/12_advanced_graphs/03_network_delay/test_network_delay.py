import pytest
from network_delay import network_delay_time


@pytest.mark.parametrize("name, times, n, k, want", [
    ("standard case", [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
    ("unreachable node", [[1, 2, 1]], 2, 2, -1),
    ("single node", [], 1, 1, 0),
    ("two paths different weights", [[1, 2, 1], [1, 3, 4], [2, 3, 2]], 3, 1, 3),
    ("all connected from source", [[1, 2, 5], [1, 3, 2], [1, 4, 9]], 4, 1, 9),
    ("chain of nodes", [[1, 2, 1], [2, 3, 2], [3, 4, 3]], 4, 1, 6),
])
def test_network_delay_time(name, times, n, k, want):
    result = network_delay_time(times, n, k)
    assert result == want, f"{name}: got {result}, want {want}"
