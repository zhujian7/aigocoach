import pytest
from trie import Trie


@pytest.mark.parametrize("name,inserts,searches,prefixes", [
    (
        "basic operations",
        ["apple"],
        [("apple", True), ("app", False), ("apples", False)],
        [("app", True), ("apple", True), ("b", False)],
    ),
    (
        "multiple words",
        ["apple", "app", "banana"],
        [("apple", True), ("app", True), ("banana", True), ("ban", False)],
        [("app", True), ("ban", True), ("cat", False)],
    ),
    (
        "empty string",
        [""],
        [("", True), ("a", False)],
        [("", True)],
    ),
    (
        "single char words",
        ["a", "b", "c"],
        [("a", True), ("b", True), ("d", False)],
        [("a", True), ("d", False)],
    ),
    (
        "overlapping words",
        ["the", "then", "them", "there"],
        [("the", True), ("then", True), ("they", False), ("there", True)],
        [("the", True), ("th", True), ("thx", False)],
    ),
])
def test_trie(name, inserts, searches, prefixes):
    t = Trie()
    for word in inserts:
        t.insert(word)
    for word, want in searches:
        got = t.search(word)
        assert got == want, f"{name}: search({word!r}) = {got}, want {want}"
    for prefix, want in prefixes:
        got = t.starts_with(prefix)
        assert got == want, f"{name}: starts_with({prefix!r}) = {got}, want {want}"
