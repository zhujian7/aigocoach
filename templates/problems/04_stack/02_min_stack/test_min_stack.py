import pytest
from min_stack import MinStack


@pytest.mark.parametrize("name, operations, values, expected", [
    ("basic push and get min", ["Push", "Push", "Push", "GetMin", "Pop", "Top", "GetMin"], [-2, 0, -3, 0, 0, 0, 0], [0, 0, 0, -3, 0, 0, -2]),
    ("single element", ["Push", "Top", "GetMin"], [5, 0, 0], [0, 5, 5]),
    ("decreasing order", ["Push", "Push", "Push", "GetMin", "Pop", "GetMin"], [3, 2, 1, 0, 0, 0], [0, 0, 0, 1, 0, 2]),
    ("increasing order", ["Push", "Push", "Push", "GetMin", "Pop", "GetMin"], [1, 2, 3, 0, 0, 0], [0, 0, 0, 1, 0, 1]),
    ("duplicate minimums", ["Push", "Push", "Push", "GetMin", "Pop", "GetMin"], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1]),
])
def test_min_stack(name, operations, values, expected):
    obj = MinStack()
    for i, op in enumerate(operations):
        if op == "Push":
            obj.push(values[i])
        elif op == "Pop":
            obj.pop()
        elif op == "Top":
            assert obj.top() == expected[i], f"{name} step {i}: Top"
        elif op == "GetMin":
            assert obj.get_min() == expected[i], f"{name} step {i}: GetMin"
