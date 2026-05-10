import pytest
from alien_dictionary import alien_order


@pytest.mark.parametrize("name, words, want", [
    ("standard order", ["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
    ("simple two words", ["z", "x"], "zx"),
    ("invalid order", ["z", "x", "z"], ""),
    ("single word", ["abc"], "abc"),
    ("prefix violation", ["abc", "ab"], ""),
    ("single characters", ["z", "z"], "z"),
])
def test_alien_order(name, words, want):
    result = alien_order(words)
    assert result == want, f"{name}: got {result}, want {want}"
