# Pacific Atlantic Water Flow

- **Difficulty**: Medium
- **Category**: Graphs
- **Topics**: DFS, BFS, matrix
- **Link**: [NeetCode](https://neetcode.io/problems/pacific-atlantic-water-flow) | [LeetCode 417](https://leetcode.com/problems/pacific-atlantic-water-flow/)

## Description

![pacific-atlantic-water-flow](assets/waterflow-grid.jpg)

There is an `m x n` rectangular island that borders both the Pacific Ocean and the Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells and you are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

Rain water can flow from a cell to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates `[r, c]` where rain water can flow to both the Pacific and Atlantic oceans.

## Examples

**Example 1:**

```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Example 2:**

```
Input: heights = [[1]]
Output: [[0,0]]
```

**Example 3:**

```
Input: heights = [[1,1],[1,1]]
Output: [[0,0],[0,1],[1,0],[1,1]]
Explanation: On a flat grid, water from every cell can reach both oceans.
```

## Constraints

- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`

## Function Signature

**Go:**

```go
func pacificAtlantic(heights [][]int) [][]int
```

**Python:**
```python
def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
```
