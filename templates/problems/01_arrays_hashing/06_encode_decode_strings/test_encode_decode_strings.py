import pytest
from encode_decode_strings import encode, decode


@pytest.mark.parametrize("name,strs", [
    ("basic strings", ["hello", "world"]),
    ("empty list", []),
    ("single empty string", [""]),
    ("multiple empty strings", ["", "", ""]),
    ("strings with special characters", ["he:llo", "wor#ld", "foo;bar"]),
    ("strings with delimiters and colons", ["4:abcd", "3:xyz"]),
    ("single character strings", ["a", "b", "c"]),
    ("mixed empty and non-empty", ["", "a", "", "b", ""]),
])
def test_encode_decode(name, strs):
    encoded = encode(strs)
    decoded = decode(encoded)
    assert decoded == strs, f"{name}: decode(encode({strs})) = {decoded}, want {strs}"
