# Jump Game II

- **Difficulty**: Medium
- **Category**: Greedy
- **Topics**: array, greedy, BFS
- **Link**: [NeetCode](https://neetcode.io/problems/jump-game-ii) | [LeetCode 45](https://leetcode.com/problems/jump-game-ii/)

## Description

You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at `nums[0]`. Each element `nums[i]` represents the maximum length of a forward jump from index `i`. Return the minimum number of jumps to reach `nums[n - 1]`. The test cases are generated such that you can always reach `nums[n - 1]`.

## Examples

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [2,3,0,1,4]
Output: 2
```

**Example 3:**

```
Input: nums = [0]
Output: 0
Explanation: Already at the last index, no jumps needed.
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It is guaranteed that you can reach `nums[n - 1]`.

## Function Signature

**Go:**

```go
func jump(nums []int) int
```

**Python:**
```python
def jump(nums: List[int]) -> int:
```
