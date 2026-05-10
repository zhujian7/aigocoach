import pytest
from graph_valid_tree import valid_tree


@pytest.mark.parametrize("name, n, edges, want", [
    ("valid tree", 5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
    ("has cycle", 5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    ("disconnected", 4, [[0, 1], [2, 3]], False),
    ("single node", 1, [], True),
    ("two nodes connected", 2, [[0, 1]], True),
    ("too many edges", 3, [[0, 1], [1, 2], [0, 2]], False),
])
def test_valid_tree(name, n, edges, want):
    result = valid_tree(n, edges)
    assert result == want, f"{name}: got {result}, want {want}"
