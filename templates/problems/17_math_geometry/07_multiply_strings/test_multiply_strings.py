import pytest
from multiply_strings import multiply


@pytest.mark.parametrize("name, num1, num2, expected", [
    ("example 1", "2", "3", "6"),
    ("example 2", "123", "456", "56088"),
    ("multiply by zero", "0", "52", "0"),
    ("both zeros", "0", "0", "0"),
    ("single digits", "9", "9", "81"),
    ("large numbers", "999", "999", "998001"),
    ("one and number", "1", "12345", "12345"),
])
def test_multiply(name, num1, num2, expected):
    result = multiply(num1, num2)
    assert result == expected, f"{name}: got {result}, want {expected}"
