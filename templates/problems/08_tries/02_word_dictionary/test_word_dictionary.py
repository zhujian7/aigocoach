import pytest
from word_dictionary import WordDictionary


@pytest.mark.parametrize("name,adds,searches", [
    (
        "basic with wildcards",
        ["bad", "dad", "mad"],
        [("pad", False), ("bad", True), (".ad", True),
         ("b..", True), ("...", True), ("....", False)],
    ),
    (
        "exact match only",
        ["hello"],
        [("hello", True), ("hell", False), ("helloo", False)],
    ),
    (
        "all wildcards",
        ["ab", "cd"],
        [("..", True), (".", False), ("...", False)],
    ),
    (
        "single char",
        ["a"],
        [(".", True), ("a", True), ("..", False)],
    ),
    (
        "mixed wildcards",
        ["apple", "ample"],
        [("a.ple", True), ("a..le", True), ("a...e", True),
         ("a....", True), ("b....", False)],
    ),
    (
        "no words added",
        [],
        [("a", False), (".", False)],
    ),
])
def test_word_dictionary(name, adds, searches):
    wd = WordDictionary()
    for word in adds:
        wd.add_word(word)
    for word, want in searches:
        got = wd.search(word)
        assert got == want, f"{name}: search({word!r}) = {got}, want {want}"
