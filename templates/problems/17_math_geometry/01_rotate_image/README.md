# Rotate Image

- **Difficulty**: Medium
- **Category**: Math & Geometry
- **Topics**: array, matrix, math
- **Link**: [NeetCode](https://neetcode.io/problems/rotate-image) | [LeetCode 48](https://leetcode.com/problems/rotate-image/)

## Description

You are given an `n x n` 2D matrix representing an image. Rotate the image by 90 degrees clockwise. You must rotate the image in-place, which means you have to modify the input 2D matrix directly. Do not allocate another 2D matrix for the rotation.

## Examples

**Example 1:**

![Example 1](assets/mat1.jpg)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Explanation: The matrix is rotated 90 degrees clockwise.
```

**Example 2:**

![Example 2](assets/mat2.jpg)

```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Explanation: The 4x4 matrix is rotated 90 degrees clockwise.
```

**Example 3:**

```
Input: matrix = [[1]]
Output: [[1]]
Explanation: A 1x1 matrix remains unchanged after rotation.
```

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Function Signature

**Go:**

```go
func rotate(matrix [][]int)
```

**Python:**
```python
def rotate(matrix: List[List[int]]) -> None:
```
