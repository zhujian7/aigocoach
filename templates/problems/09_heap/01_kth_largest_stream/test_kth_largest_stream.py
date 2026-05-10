import pytest
from kth_largest_stream import KthLargest


@pytest.mark.parametrize("name,k,nums,adds,expects", [
    ("example from problem", 3, [4, 5, 8, 2], [3, 5, 10, 9, 4], [4, 5, 5, 8, 8]),
    ("k equals 1", 1, [], [-1, 1, -2, -4, 3], [-1, 1, 1, 1, 3]),
    ("single initial element", 1, [5], [3, 7], [5, 7]),
    ("all same values", 2, [0], [0, 0, 0], [0, 0, 0]),
    ("negative numbers", 2, [-5, -3], [-1, -7, 0], [-3, -3, -1]),
    ("large k with enough initial elements", 3, [1, 2, 3, 4, 5], [6], [4]),
])
def test_kth_largest(name, k, nums, adds, expects):
    kl = KthLargest(k, nums)
    for i, val in enumerate(adds):
        got = kl.add(val)
        assert got == expects[i], (
            f"{name}: add({val}) = {got}, want {expects[i]}"
        )
