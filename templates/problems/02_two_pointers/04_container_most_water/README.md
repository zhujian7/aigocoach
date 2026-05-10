# Container With Most Water

- **Difficulty**: Medium
- **Category**: Two Pointers
- **Topics**: array, two pointers, greedy
- **Link**: [NeetCode](https://neetcode.io/problems/max-water-container) | [LeetCode 11](https://leetcode.com/problems/container-with-most-water/)

## Description

![container-with-most-water](assets/question_11.jpg)

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

Notice that you may not slant the container.

## Examples

**Example 1:**

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The lines at index 1 (height 8) and index 8 (height 7) form a container with width 7. The area is min(8,7) * 7 = 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

**Example 3:**

```
Input: height = [4,3,2,1,4]
Output: 16
Explanation: The lines at index 0 (height 4) and index 4 (height 4) form a container with width 4. The area is min(4,4) * 4 = 16.
```

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Function Signature

**Go:**

```go
func maxArea(height []int) int
```

**Python:**
```python
def max_area(height: List[int]) -> int:
```
