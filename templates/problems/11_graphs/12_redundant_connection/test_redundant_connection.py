import pytest
from redundant_connection import find_redundant_connection


@pytest.mark.parametrize("name, edges, want", [
    ("triangle", [[1, 2], [1, 3], [2, 3]], [2, 3]),
    ("four nodes with cycle", [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
    ("last edge creates cycle", [[1, 2], [1, 3], [3, 4], [2, 4]], [2, 4]),
    ("two nodes", [[1, 2], [2, 1]], [2, 1]),
    ("five node cycle", [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]], [5, 1]),
    ("star with extra edge", [[1, 2], [1, 3], [1, 4], [3, 4]], [3, 4]),
])
def test_find_redundant_connection(name, edges, want):
    result = find_redundant_connection(edges)
    assert result == want, f"{name}: got {result}, want {want}"
