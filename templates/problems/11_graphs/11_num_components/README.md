# Number of Connected Components in an Undirected Graph

- **Difficulty**: Medium
- **Category**: Graphs
- **Topics**: union find, graph, connected components
- **Link**: [NeetCode](https://neetcode.io/problems/count-connected-components) | [LeetCode 323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [LintCode 431](https://www.lintcode.com/problem/431/)

## Description

You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi`.

Return the number of connected components in the graph. A connected component is a maximal set of nodes such that there is a path between every pair of nodes in it.

## Examples

**Example 1:**

```
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Explanation: Components are {0,1,2} and {3,4}.
```

**Example 2:**

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
Explanation: All nodes are connected in a single component.
```

**Example 3:**

```
Input: n = 4, edges = []
Output: 4
Explanation: No edges means each node is its own component.
```

## Constraints

- `1 <= n <= 2000`
- `1 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- There are no repeated edges.

## Function Signature

**Go:**

```go
func countComponents(n int, edges [][]int) int
```

**Python:**
```python
def count_components(n: int, edges: List[List[int]]) -> int:
```
