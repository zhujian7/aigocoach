import pytest
from reconstruct_itinerary import find_itinerary


@pytest.mark.parametrize("name, tickets, want", [
    ("standard itinerary", [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], ["JFK", "MUC", "LHR", "SFO", "SJC"]),
    ("lexical order matters", [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]], ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
    ("single ticket", [["JFK", "ATL"]], ["JFK", "ATL"]),
    ("round trip", [["JFK", "ATL"], ["ATL", "JFK"]], ["JFK", "ATL", "JFK"]),
    ("three cities chain", [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]], ["JFK", "NRT", "JFK", "KUL"]),
    ("duplicate tickets", [["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"], ["ATL", "SFO"]], ["JFK", "ATL", "JFK", "ATL", "SFO"]),
])
def test_find_itinerary(name, tickets, want):
    result = find_itinerary(tickets)
    assert result == want, f"{name}: got {result}, want {want}"
