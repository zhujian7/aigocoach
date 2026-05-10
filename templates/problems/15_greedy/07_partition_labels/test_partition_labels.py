import pytest
from partition_labels import partition_labels


@pytest.mark.parametrize("name, s, expected", [
    ("example 1", "ababcbacadefegdehijhklij", [9, 7, 8]),
    ("single char", "a", [1]),
    ("all same", "aaaa", [4]),
    ("all unique", "abcdef", [1, 1, 1, 1, 1, 1]),
    ("two partitions", "aabbb", [2, 3]),
    ("example 2", "eccbbbbdec", [10]),
    ("interleaved", "abac", [3, 1]),
])
def test_partition_labels(name, s, expected):
    result = partition_labels(s)
    assert result == expected, f"{name}: got {result}, want {expected}"
