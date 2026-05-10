# Network Delay Time

- **Difficulty**: Medium
- **Category**: Advanced Graphs
- **Topics**: Dijkstra's algorithm, heap, shortest path, weighted graph
- **Link**: [NeetCode](https://neetcode.io/problems/network-delay-time) | [LeetCode 743](https://leetcode.com/problems/network-delay-time/)

## Description

![network-delay-time](assets/931_example_1.png)

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return the minimum time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

## Examples

**Example 1:**

```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Explanation: Signal from node 2 reaches node 1 in 1 unit, node 3 in 1 unit, and node 4 in 2 units.
```

**Example 2:**

```
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
Explanation: Node 1 cannot be reached from node 2.
```

**Example 3:**

```
Input: times = [], n = 1, k = 1
Output: 0
Explanation: Only one node, signal is already there.
```

## Constraints

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= ui, vi <= n`
- `ui != vi`
- `0 <= wi <= 100`
- All the pairs `(ui, vi)` are unique (no multiple edges).

## Function Signature

**Go:**

```go
func networkDelayTime(times [][]int, n int, k int) int
```

**Python:**
```python
def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
```
