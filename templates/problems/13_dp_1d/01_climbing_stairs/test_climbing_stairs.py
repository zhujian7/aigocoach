import pytest
from climbing_stairs import climb_stairs


@pytest.mark.parametrize("name, n, want", [
    ("one step", 1, 1),
    ("two steps", 2, 2),
    ("three steps", 3, 3),
    ("four steps", 4, 5),
    ("five steps", 5, 8),
    ("ten steps", 10, 89),
])
def test_climb_stairs(name, n, want):
    result = climb_stairs(n)
    assert result == want, f"{name}: got {result}, want {want}"
