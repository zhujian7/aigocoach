# Non-Overlapping Intervals

- **Difficulty**: Medium
- **Category**: Intervals
- **Topics**: array, greedy, sorting, intervals
- **Link**: [NeetCode](https://neetcode.io/problems/non-overlapping-intervals) | [LeetCode 435](https://leetcode.com/problems/non-overlapping-intervals/)

## Description

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Two intervals `[a, b]` and `[c, d]` are considered overlapping if they share any interior point, i.e., `a < d` and `c < b`. Intervals that only touch at a boundary point (e.g., `[1, 2]` and `[2, 3]`) are not overlapping.

## Examples

**Example 1:**

```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: Removing [1,3] makes the rest [[1,2],[2,3],[3,4]] non-overlapping.
```

**Example 2:**

```
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: The intervals do not overlap (they only touch at point 2), so no removal is needed.
```

**Example 3:**

```
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: Two of the three identical intervals must be removed.
```

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

## Function Signature

**Go:**

```go
func eraseOverlapIntervals(intervals [][]int) int
```

**Python:**
```python
def erase_overlap_intervals(intervals: List[List[int]]) -> int:
```
