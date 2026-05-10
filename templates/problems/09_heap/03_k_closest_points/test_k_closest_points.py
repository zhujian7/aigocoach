import pytest
from k_closest_points import k_closest


def dist(p):
    return p[0] * p[0] + p[1] * p[1]


def sort_2d(lst):
    if lst is None:
        return None
    return sorted([sorted(sub) for sub in lst])


@pytest.mark.parametrize("name, points, k, want", [
    ("example 1", [[1, 3], [-2, 2]], 1, [[-2, 2]]),
    ("example 2", [[3, 3], [5, -1], [-2, 4]], 2, [[-2, 4], [3, 3]]),
    ("single point", [[0, 1]], 1, [[0, 1]]),
    ("all points same distance", [[1, 0], [0, 1], [-1, 0], [0, -1]], 2, None),
    ("origin point", [[0, 0], [1, 1], [2, 2]], 1, [[0, 0]]),
    ("k equals length", [[1, 2], [3, 4]], 2, [[1, 2], [3, 4]]),
])
def test_k_closest(name, points, k, want):
    result = k_closest(points, k)
    if want is None:
        # All points are equidistant; just verify k points returned
        # and all have correct distance
        assert len(result) == k, f"{name}: got {len(result)} points, want {k}"
        max_dist = max(dist(p) for p in result)
        # All returned points should have distance <= max distance of any k points
        all_dists = sorted(dist(p) for p in points)
        assert max_dist <= all_dists[k - 1], (
            f"{name}: returned point with dist {max_dist} > kth dist {all_dists[k - 1]}"
        )
    else:
        assert sort_2d(result) == sort_2d(want), f"{name}: got {result}, want {want}"
