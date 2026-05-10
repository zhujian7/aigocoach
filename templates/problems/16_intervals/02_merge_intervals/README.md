# Merge Intervals

- **Difficulty**: Medium
- **Category**: Intervals
- **Topics**: array, sorting, intervals
- **Link**: [NeetCode](https://neetcode.io/problems/merge-intervals) | [LeetCode 56](https://leetcode.com/problems/merge-intervals/)

## Description

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input. Two intervals are considered overlapping if they share at least one common point (e.g., `[1,4]` and `[4,5]` overlap).

The input intervals are not necessarily sorted.

## Examples

**Example 1:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Intervals [1,3] and [2,6] overlap, so they are merged into [1,6].
```

**Example 2:**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping since they share the point 4.
```

**Example 3:**

```
Input: intervals = [[1,4],[2,5],[3,6]]
Output: [[1,6]]
Explanation: All three intervals overlap and merge into a single interval [1,6].
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Function Signature

**Go:**

```go
func merge(intervals [][]int) [][]int
```

**Python:**
```python
def merge(intervals: List[List[int]]) -> List[List[int]]:
```
