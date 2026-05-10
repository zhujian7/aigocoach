# Meeting Rooms II

- **Difficulty**: Medium
- **Category**: Intervals
- **Topics**: array, sorting, heap, intervals, sweep line
- **Link**: [NeetCode](https://neetcode.io/problems/meeting-schedule-ii) | [LeetCode 253](https://leetcode.com/problems/meeting-rooms-ii/) | [LintCode 919](https://www.lintcode.com/problem/919/)

## Description

Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, find the minimum number of conference rooms required so that all meetings can take place without conflicts. Two meetings can use the same room if one ends before or exactly when the other starts.

## Examples

**Example 1:**

```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation: Meeting [0,30] occupies one room. Meetings [5,10] and [15,20] can share a second room since [15,20] starts after [5,10] ends.
```

**Example 2:**

```
Input: intervals = [[7,10],[2,4]]
Output: 1
Explanation: The meetings do not overlap, so only one room is needed.
```

**Example 3:**

```
Input: intervals = [[1,5],[2,6],[3,7]]
Output: 3
Explanation: All three meetings overlap with each other, so three rooms are needed.
```

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^6`

## Function Signature

**Go:**

```go
func minMeetingRooms(intervals [][]int) int
```

**Python:**
```python
def min_meeting_rooms(intervals: List[List[int]]) -> int:
```
