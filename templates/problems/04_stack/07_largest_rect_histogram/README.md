# Largest Rectangle in Histogram

- **Difficulty**: Hard
- **Category**: Stack
- **Topics**: stack, monotonic stack, array
- **Link**: [NeetCode](https://neetcode.io/problems/largest-rectangle-in-histogram) | [LeetCode 84](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## Description

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

The rectangle must be formed by contiguous bars, and its height is limited by the shortest bar within the rectangle's span.

## Examples

**Example 1:**

![Example 1](assets/histogram.jpg)

```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle has area = 5 * 2 = 10 (formed by bars at indices 2 and 3 with heights 5 and 6, taking the minimum height 5 over width 2).
```

**Example 2:**

![Example 2](assets/histogram-1.jpg)

```
Input: heights = [5]
Output: 5
Explanation: A single bar of height 5 and width 1 gives area 5.
```

**Example 3:**

```
Input: heights = [3,3,3,3]
Output: 12
Explanation: All bars have height 3, so the rectangle spans all 4 bars: 3 * 4 = 12.
```

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

## Function Signature

**Go:**

```go
func largestRectangleArea(heights []int) int
```

**Python:**
```python
def largest_rectangle_area(heights: List[int]) -> int:
```
