# Meeting Rooms

- **Difficulty**: Easy
- **Category**: Intervals
- **Topics**: array, sorting, intervals
- **Link**: [NeetCode](https://neetcode.io/problems/meeting-schedule) | [LeetCode 252](https://leetcode.com/problems/meeting-rooms/) | [LintCode 920](https://www.lintcode.com/problem/920/)

## Description

Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, determine if a person could attend all meetings. A person can attend all meetings only if no two meetings overlap in time. Meetings that start exactly when another ends (e.g., `[1, 5]` and `[5, 10]`) do not conflict.

## Examples

**Example 1:**

```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation: The meeting [5,10] conflicts with [0,30] since 5 < 30.
```

**Example 2:**

```
Input: intervals = [[7,10],[2,4]]
Output: true
Explanation: The two meetings do not overlap.
```

**Example 3:**

```
Input: intervals = [[1,5],[5,10]]
Output: true
Explanation: The meetings touch at boundary point 5 but do not overlap.
```

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^6`

## Function Signature

**Go:**

```go
func canAttendMeetings(intervals [][]int) bool
```

**Python:**
```python
def can_attend_meetings(intervals: List[List[int]]) -> bool:
```
