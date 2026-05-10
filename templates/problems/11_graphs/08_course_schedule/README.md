# Course Schedule

- **Difficulty**: Medium
- **Category**: Graphs
- **Topics**: DFS, topological sort, cycle detection, directed graph
- **Link**: [NeetCode](https://neetcode.io/problems/course-schedule) | [LeetCode 207](https://leetcode.com/problems/course-schedule/)

## Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]` indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

## Examples

**Example 1:**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: You take course 0 first, then course 1.
```

**Example 2:**

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: Courses 0 and 1 depend on each other, creating a cycle.
```

**Example 3:**

```
Input: numCourses = 3, prerequisites = []
Output: true
Explanation: No prerequisites, all courses can be taken independently.
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- All the pairs `prerequisites[i]` are unique.

## Function Signature

**Go:**

```go
func canFinish(numCourses int, prerequisites [][]int) bool
```

**Python:**
```python
def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
```
