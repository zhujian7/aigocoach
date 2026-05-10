# Reconstruct Itinerary

- **Difficulty**: Hard
- **Category**: Advanced Graphs
- **Topics**: Eulerian path, DFS, Hierholzer's algorithm, greedy
- **Link**: [NeetCode](https://neetcode.io/problems/reconstruct-flight-path) | [LeetCode 332](https://leetcode.com/problems/reconstruct-itinerary/)

## Description

You are given a list of airline `tickets` where `tickets[i] = [fromi, toi]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`, thus the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

You may assume all tickets form at least one valid itinerary. You must use all the tickets exactly once.

## Examples

**Example 1:**

![Example 1](assets/itinerary1-graph.jpg)

```
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

**Example 2:**

![Example 2](assets/itinerary2-graph.jpg)

```
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another valid itinerary would be ["JFK","SFO","ATL","JFK","ATL","SFO"] but it has a larger lexical order.
```

**Example 3:**

```
Input: tickets = [["JFK","ATL"],["ATL","JFK"]]
Output: ["JFK","ATL","JFK"]
```

## Constraints

- `1 <= tickets.length <= 300`
- `tickets[i].length == 2`
- `fromi.length == 3`
- `toi.length == 3`
- `fromi` and `toi` consist of uppercase English letters.
- `fromi != toi`

## Function Signature

**Go:**

```go
func findItinerary(tickets [][]string) []string
```

**Python:**
```python
def find_itinerary(tickets: List[List[str]]) -> List[str]:
```
