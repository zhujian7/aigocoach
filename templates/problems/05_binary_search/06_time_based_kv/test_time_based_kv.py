import pytest
from time_based_kv import TimeMap


@pytest.mark.parametrize("name, operations, keys, values, timestamps, expected", [
    ("basic set and get", ["Set", "Get", "Get", "Set", "Get", "Get"], ["foo", "foo", "foo", "foo", "foo", "foo"], ["bar", "", "", "bar2", "", ""], [1, 1, 3, 4, 4, 5], ["", "bar", "bar", "", "bar2", "bar2"]),
    ("get before any set", ["Get"], ["foo"], [""], [1], [""]),
    ("get with timestamp before first set", ["Set", "Get"], ["key", "key"], ["val", ""], [5, 3], ["", ""]),
    ("multiple keys", ["Set", "Set", "Get", "Get"], ["a", "b", "a", "b"], ["v1", "v2", "", ""], [1, 1, 1, 1], ["", "", "v1", "v2"]),
    ("get exact timestamp", ["Set", "Set", "Set", "Get", "Get", "Get"], ["k", "k", "k", "k", "k", "k"], ["a", "b", "c", "", "", ""], [1, 2, 3, 1, 2, 3], ["", "", "", "a", "b", "c"]),
])
def test_time_map(name, operations, keys, values, timestamps, expected):
    obj = TimeMap()
    for i, op in enumerate(operations):
        if op == "Set":
            obj.set(keys[i], values[i], timestamps[i])
        elif op == "Get":
            result = obj.get(keys[i], timestamps[i])
            assert result == expected[i], f"{name} step {i}: Get({keys[i]}, {timestamps[i]}) = {result}, want {expected[i]}"
