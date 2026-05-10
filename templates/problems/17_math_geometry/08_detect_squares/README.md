# Detect Squares

- **Difficulty**: Medium
- **Category**: Math & Geometry
- **Topics**: array, hash table, design, counting
- **Link**: [NeetCode](https://neetcode.io/problems/count-squares) | [LeetCode 2013](https://leetcode.com/problems/detect-squares/)

## Description

![detect-squares](assets/image.png)

You are given a stream of points on the X-Y plane. Design a data structure that supports the following operations:

- **Add** a new point to the data structure. Duplicate points are allowed and should be counted separately.
- **Count** the number of ways to form axis-aligned squares with a given query point as one of the four corners. An axis-aligned square has all sides parallel to the X-axis and Y-axis, and has a positive area (side length > 0).

Implement the `DetectSquares` struct with `Constructor()`, `Add(point []int)`, and `Count(point []int) int`.

## Examples

**Example 1:**

```
Input:
  Add points: [3,10], [11,10], [11,2]
  Count query: [3,2]
Output: 1
Explanation: Points [3,10], [11,10], [11,2], and query [3,2] form one axis-aligned square with side length 8.
```

**Example 2:**

```
Input:
  Add points: [3,10], [3,10], [11,10], [11,2]
  Count query: [3,2]
Output: 2
Explanation: The duplicate point [3,10] allows two distinct squares to be counted.
```

**Example 3:**

```
Input:
  Add points: [1,1], [2,2]
  Count query: [3,3]
Output: 0
Explanation: No axis-aligned square can be formed with the query point.
```

## Constraints

- `point.length == 2`
- `0 <= x, y <= 1000`
- At most `3000` calls in total will be made to `Add` and `Count`

## Function Signature

**Go:**

```go
type DetectSquares struct {}

func Constructor() DetectSquares

func (ds *DetectSquares) Add(point []int)

func (ds *DetectSquares) Count(point []int) int
```

**Python:**
```python
class DetectSquares
def __init__(self):
def add(self, point: List[int]) -> None:
def count(self, point: List[int]) -> int:
```
