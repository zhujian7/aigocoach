import pytest
from detect_squares import DetectSquares


@pytest.mark.parametrize("name,add_points,query_point,expected", [
    ("basic square", [[3, 10], [11, 10], [11, 2]], [3, 2], 1),
    ("no square possible", [[1, 1], [2, 2]], [3, 3], 0),
    (
        "duplicate points multiply count",
        [[3, 10], [3, 10], [11, 10], [11, 2]],
        [3, 2],
        2,
    ),
    (
        "multiple squares from one query",
        [[0, 0], [1, 0], [1, 1], [0, 1], [2, 0], [2, 2], [0, 2]],
        [0, 0],
        2,
    ),
    ("no points added", [], [0, 0], 0),
    ("collinear points", [[1, 1], [2, 1], [3, 1]], [0, 1], 0),
])
def test_detect_squares(name, add_points, query_point, expected):
    ds = DetectSquares()
    for p in add_points:
        ds.add(p)
    got = ds.count(query_point)
    assert got == expected, (
        f"{name}: count({query_point}) = {got}, want {expected}"
    )
