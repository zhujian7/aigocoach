# Spiral Matrix

- **Difficulty**: Medium
- **Category**: Math & Geometry
- **Topics**: array, matrix, simulation
- **Link**: [NeetCode](https://neetcode.io/problems/spiral-matrix) | [LeetCode 54](https://leetcode.com/problems/spiral-matrix/)

## Description

Given an `m x n` matrix, return all elements of the matrix in spiral order. Starting from the top-left corner, traverse the matrix in a clockwise spiral: move right along the top row, down along the right column, left along the bottom row, and up along the left column, then repeat for the inner layers.

## Examples

**Example 1:**

![Example 1](assets/spiral1.jpg)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Explanation: Spiral order traversal of the 3x3 matrix.
```

**Example 2:**

![Example 2](assets/spiral.jpg)

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Explanation: Spiral order traversal of the 3x4 matrix.
```

**Example 3:**

```
Input: matrix = [[1]]
Output: [1]
Explanation: A single-element matrix has only one element in spiral order.
```

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Function Signature

**Go:**

```go
func spiralOrder(matrix [][]int) []int
```

**Python:**
```python
def spiral_order(matrix: List[List[int]]) -> List[int]:
```
