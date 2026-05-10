import pytest
from num_islands import num_islands


@pytest.mark.parametrize("name, grid, want", [
    ("single island", [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]], 1),
    ("three islands", [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]], 3),
    ("all water", [["0", "0", "0"], ["0", "0", "0"]], 0),
    ("all land", [["1", "1"], ["1", "1"]], 1),
    ("diagonal islands", [["1", "0"], ["0", "1"]], 2),
    ("single cell land", [["1"]], 1),
    ("single cell water", [["0"]], 0),
])
def test_num_islands(name, grid, want):
    result = num_islands(grid)
    assert result == want, f"{name}: got {result}, want {want}"
