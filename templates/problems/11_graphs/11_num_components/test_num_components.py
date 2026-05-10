import pytest
from num_components import count_components


@pytest.mark.parametrize("name, n, edges, want", [
    ("two components", 5, [[0, 1], [1, 2], [3, 4]], 2),
    ("one component", 5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
    ("all isolated", 4, [], 4),
    ("single node", 1, [], 1),
    ("three components", 6, [[0, 1], [2, 3], [4, 5]], 3),
    ("fully connected", 3, [[0, 1], [1, 2], [0, 2]], 1),
])
def test_count_components(name, n, edges, want):
    result = count_components(n, edges)
    assert result == want, f"{name}: got {result}, want {want}"
