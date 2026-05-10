import pytest
from find_median_stream import MedianFinder


@pytest.mark.parametrize("name,adds,medians", [
    ("example from problem", [1, 2, 3], [1.0, 1.5, 2.0]),
    ("single element", [5], [5.0]),
    ("two elements", [1, 2], [1.0, 1.5]),
    ("negative numbers", [-1, -2, -3], [-1.0, -1.5, -2.0]),
    ("duplicates", [1, 1, 1, 1], [1.0, 1.0, 1.0, 1.0]),
    ("descending order", [5, 4, 3, 2, 1], [5.0, 4.5, 4.0, 3.5, 3.0]),
    ("large gap", [0, 100], [0.0, 50.0]),
])
def test_median_finder(name, adds, medians):
    mf = MedianFinder()
    for i, num in enumerate(adds):
        mf.add_num(num)
        got = mf.find_median()
        assert abs(got - medians[i]) < 1e-5, (
            f"{name}: after add_num({num}), "
            f"find_median() = {got}, want {medians[i]}"
        )
