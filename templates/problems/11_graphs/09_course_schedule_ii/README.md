# Course Schedule II

- **Difficulty**: Medium
- **Category**: Graphs
- **Topics**: topological sort, BFS, Kahn's algorithm, directed graph
- **Link**: [NeetCode](https://neetcode.io/problems/course-schedule-ii) | [LeetCode 210](https://leetcode.com/problems/course-schedule-ii/)

## Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

Return the ordering of courses you should take to finish all courses. If there are multiple valid orderings, return any of them. If it is impossible to finish all courses (due to a cycle), return an empty array.

## Examples

**Example 1:**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: Take course 0 first, then course 1.
```

**Example 2:**

```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are multiple valid orderings. Course 0 must come first.
```

**Example 3:**

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: []
Explanation: A cycle exists, so no valid ordering is possible.
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `ai != bi`
- All the pairs `[ai, bi]` are distinct.

## Function Signature

**Go:**

```go
func findOrder(numCourses int, prerequisites [][]int) []int
```

**Python:**
```python
def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
```
