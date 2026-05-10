# Task Scheduler

- **Difficulty**: Medium
- **Category**: Heap
- **Topics**: max-heap, greedy, scheduling
- **Link**: [NeetCode](https://neetcode.io/problems/task-scheduling) | [LeetCode 621](https://leetcode.com/problems/task-scheduler/)

## Description

You are given an array of CPU tasks, each represented by a character (A to Z), and a cooling interval `n`. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least `n` intervals. If no task can be scheduled during a cooling interval, the CPU remains idle. Return the minimum number of intervals the CPU will take to finish all the given tasks.

## Examples

**Example 1:**

```
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: One possible schedule: A B idle A B idle A B. Tasks A and B each appear 3 times and must be separated by at least 2 intervals.
```

**Example 2:**

```
Input: tasks = ['A','A','A','B','B','B'], n = 0
Output: 6
Explanation: With no cooldown, tasks can be executed back to back: ABABAB or any order. Total 6 intervals.
```

**Example 3:**

```
Input: tasks = ['A','A','A','A','A','A','B','C','D','E','F','G'], n = 2
Output: 16
Explanation: One possible schedule: A B C A D E A F G A idle idle A idle idle A. Task A appears 6 times and dominates the schedule.
```

## Constraints

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter.
- `0 <= n <= 100`

## Function Signature

**Go:**

```go
func leastInterval(tasks []byte, n int) int
```

**Python:**
```python
def least_interval(tasks: str, n: int) -> int:
```
