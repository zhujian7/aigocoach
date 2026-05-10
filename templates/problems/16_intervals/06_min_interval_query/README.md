# Minimum Interval to Include Each Query

- **Difficulty**: Hard
- **Category**: Intervals
- **Topics**: array, sorting, heap, intervals
- **Link**: [NeetCode](https://neetcode.io/problems/minimum-interval-including-query) | [LeetCode 1851](https://leetcode.com/problems/minimum-interval-to-include-each-query/)

## Description

You are given a 2D integer array `intervals` where `intervals[i] = [left_i, right_i]` describes the `i`-th interval starting at `left_i` and ending at `right_i` (inclusive). The size of an interval is defined as the number of integers it contains, or more formally `right_i - left_i + 1`.

You are also given an integer array `queries`. The answer to the `j`-th query is the size of the smallest interval `i` such that `left_i <= queries[j] <= right_i`. If no such interval exists, the answer is `-1`.

Return an array containing the answers to the queries.

## Examples

**Example 1:**

```
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation:
- Query 2: intervals [1,4] (size 4) and [2,4] (size 3) contain 2. Smallest is 3.
- Query 3: intervals [1,4] (size 4), [2,4] (size 3), and [3,6] (size 4) contain 3. Smallest is 3.
- Query 4: all four intervals contain 4. [4,4] (size 1) is the smallest.
- Query 5: only [3,6] (size 4) contains 5.
```

**Example 2:**

```
Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation:
- Query 2: [2,3] (size 2) is the smallest containing 2.
- Query 19: no interval contains 19, so -1.
- Query 5: [2,5] (size 4) is the smallest containing 5.
- Query 22: [20,25] (size 6) contains 22.
```

## Constraints

- `1 <= intervals.length <= 10^5`
- `1 <= queries.length <= 10^5`
- `intervals[i].length == 2`
- `1 <= left_i <= right_i <= 10^7`
- `1 <= queries[j] <= 10^7`

## Function Signature

**Go:**

```go
func minInterval(intervals [][]int, queries []int) []int
```

**Python:**
```python
def min_interval(intervals: List[List[int]], queries: List[int]) -> List[int]:
```
