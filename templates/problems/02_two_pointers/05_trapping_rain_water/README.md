# Trapping Rain Water

- **Difficulty**: Hard
- **Category**: Two Pointers
- **Topics**: array, two pointers, dynamic programming, stack
- **Link**: [NeetCode](https://neetcode.io/problems/trapping-rain-water) | [LeetCode 42](https://leetcode.com/problems/trapping-rain-water/)

## Description

![trapping-rain-water](assets/rainwatertrap.png)

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

The amount of water that can be trapped above each bar is determined by the minimum of the maximum height to its left and the maximum height to its right, minus the bar's own height. If this value is negative, no water is trapped at that position.

## Examples

**Example 1:**

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map traps 6 units of rain water. Water fills the gaps between the bars.
```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

**Example 3:**

```
Input: height = [1,2,3,4,5]
Output: 0
Explanation: No water can be trapped because the bars are in strictly increasing order.
```

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Function Signature

**Go:**

```go
func trap(height []int) int
```

**Python:**
```python
def trap(height: List[int]) -> int:
```
