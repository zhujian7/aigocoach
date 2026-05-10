import pytest
from generate_parentheses import generate_parenthesis


@pytest.mark.parametrize("name, n, want", [
    ("n=1", 1, ["()"]),
    ("n=2", 2, ["(())", "()()"]),
    ("n=3", 3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ("n=4 count", 4, None),
])
def test_generate_parenthesis(name, n, want):
    result = generate_parenthesis(n)
    if want is None:
        # n=4 Catalan number is 14
        assert len(result) == 14, f"{name}: got {len(result)} results, want 14"
    else:
        assert sorted(result) == sorted(want), f"{name}: got {result}, want {want}"
