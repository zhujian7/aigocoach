import pytest
from lru_cache import LRUCache


@pytest.mark.parametrize("name, operations, capacity, keys, values, expected", [
    ("basic get and put", ["put", "put", "get", "put", "get", "put", "get", "get", "get"], 2, [1, 2, 1, 3, 2, 4, 1, 3, 4], [1, 2, 0, 3, 0, 4, 0, 0, 0], [-2, -2, 1, -2, -1, -2, -1, 3, 4]),
    ("capacity one", ["put", "get", "put", "get", "get"], 1, [1, 1, 2, 1, 2], [10, 0, 20, 0, 0], [-2, 10, -2, -1, 20]),
    ("update existing key", ["put", "put", "get", "put", "get"], 2, [1, 1, 1, 2, 1], [1, 2, 0, 3, 0], [-2, -2, 2, -2, 2]),
    ("get miss", ["get", "put", "get", "get"], 2, [5, 5, 5, 10], [0, 50, 0, 0], [-1, -2, 50, -1]),
    ("eviction order with get refresh", ["put", "put", "get", "put", "get"], 2, [1, 2, 1, 3, 2], [1, 2, 0, 3, 0], [-2, -2, 1, -2, -1]),
])
def test_lru_cache(name, operations, capacity, keys, values, expected):
    obj = LRUCache(capacity)
    for i, op in enumerate(operations):
        if op == "put":
            obj.put(keys[i], values[i])
            assert expected[i] == -2, f"{name} step {i}: put should have -2 sentinel"
        elif op == "get":
            result = obj.get(keys[i])
            assert result == expected[i], f"{name} step {i}: get({keys[i]}) = {result}, want {expected[i]}"
