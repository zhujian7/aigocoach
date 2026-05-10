import pytest
from eval_rpn import eval_rpn


@pytest.mark.parametrize("name, tokens, want", [
    ("simple addition", ["2", "1", "+"], 3),
    ("simple subtraction", ["4", "2", "-"], 2),
    ("simple multiplication", ["3", "4", "*"], 12),
    ("simple division", ["6", "3", "/"], 2),
    ("complex expression", ["2", "1", "+", "3", "*"], 9),
    ("leetcode example", ["4", "13", "5", "/", "+"], 6),
    ("negative result", ["1", "2", "-"], -1),
    ("single number", ["42"], 42),
])
def test_eval_rpn(name, tokens, want):
    result = eval_rpn(tokens)
    assert result == want, f"{name}: got {result}, want {want}"
