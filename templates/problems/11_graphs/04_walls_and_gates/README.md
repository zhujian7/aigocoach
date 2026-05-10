# Walls and Gates

- **Difficulty**: Medium
- **Category**: Graphs
- **Topics**: BFS, multi-source BFS, matrix
- **Link**: [NeetCode](https://neetcode.io/problems/islands-and-treasure) | [LeetCode 286](https://leetcode.com/problems/walls-and-gates/) | [LintCode 663](https://www.lintcode.com/problem/663/)

## Description

You are given an `m x n` grid `rooms` initialized with these three possible values:

- `-1` -- A wall or an obstacle.
- `0` -- A gate.
- `INF` (2147483647) -- An empty room.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, the room should remain `INF`.

Distance is measured as the number of steps in the four cardinal directions (up, down, left, right).

## Examples

**Example 1:**

```
Input: rooms = [
  [INF, -1,  0, INF],
  [INF, INF, INF, -1],
  [INF, -1, INF, -1],
  [ 0,  -1, INF, INF]
]
Output: [
  [3, -1, 0,  1],
  [2,  2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3,  4]
]
```

**Example 2:**

```
Input: rooms = [[0]]
Output: [[0]]
```

**Example 3:**

```
Input: rooms = [[INF, INF],[INF, INF]]
Output: [[INF, INF],[INF, INF]]
Explanation: No gates exist, so all rooms remain INF.
```

## Constraints

- `m == rooms.length`
- `n == rooms[i].length`
- `1 <= m, n <= 250`
- `rooms[i][j]` is `-1`, `0`, or `2147483647`.

## Function Signature

**Go:**

```go
func wallsAndGates(rooms [][]int)
```

**Python:**
```python
def walls_and_gates(rooms: List[List[int]]) -> None:
```
