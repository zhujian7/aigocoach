import pytest
from unique_paths import unique_paths


@pytest.mark.parametrize("name, m, n, want", [
    ("3x7 grid", 3, 7, 28),
    ("3x2 grid", 3, 2, 3),
    ("1x1 grid", 1, 1, 1),
    ("1xN single row", 1, 5, 1),
    ("Nx1 single column", 5, 1, 1),
    ("2x2 grid", 2, 2, 2),
    ("3x3 grid", 3, 3, 6),
])
def test_unique_paths(name, m, n, want):
    result = unique_paths(m, n)
    assert result == want, f"{name}: got {result}, want {want}"
