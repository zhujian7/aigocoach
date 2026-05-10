# Daily Temperatures

- **Difficulty**: Medium
- **Category**: Stack
- **Topics**: stack, monotonic stack, array
- **Link**: [NeetCode](https://neetcode.io/problems/daily-temperatures) | [LeetCode 739](https://leetcode.com/problems/daily-temperatures/)

## Description

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

## Examples

**Example 1:**

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Explanation: For day 0, day 1 is warmer (74 > 73), so answer[0] = 1. For day 2, the next warmer day is day 6 (76 > 75), so answer[2] = 4.
```

**Example 2:**

```
Input: temperatures = [30,20,10]
Output: [0,0,0]
Explanation: Temperatures are strictly decreasing, so no day has a future warmer day.
```

**Example 3:**

```
Input: temperatures = [10,20,30]
Output: [1,1,0]
Explanation: Each day (except the last) has the next day as a warmer day.
```

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Function Signature

**Go:**

```go
func dailyTemperatures(temperatures []int) []int
```

**Python:**
```python
def daily_temperatures(temperatures: List[int]) -> List[int]:
```
