# Graph Valid Tree

- **Difficulty**: Medium
- **Category**: Graphs
- **Topics**: union find, graph, tree
- **Link**: [NeetCode](https://neetcode.io/problems/valid-tree) | [LeetCode 261](https://leetcode.com/problems/graph-valid-tree/) | [LintCode 178](https://www.lintcode.com/problem/178/)

## Description

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` if the edges of the given graph make up a valid tree, and `false` otherwise. A valid tree is a connected, acyclic undirected graph. Equivalently, a valid tree with `n` nodes has exactly `n - 1` edges and is connected.

## Examples

**Example 1:**

```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

**Example 2:**

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
Explanation: There is a cycle: 1 -> 2 -> 3 -> 1.
```

**Example 3:**

```
Input: n = 4, edges = [[0,1],[2,3]]
Output: false
Explanation: The graph is disconnected (two separate components).
```

## Constraints

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- There are no self-loops or repeated edges.

## Function Signature

**Go:**

```go
func validTree(n int, edges [][]int) bool
```

**Python:**
```python
def valid_tree(n: int, edges: List[List[int]]) -> bool:
```
