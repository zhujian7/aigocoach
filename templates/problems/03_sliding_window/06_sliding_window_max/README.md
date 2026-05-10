# Sliding Window Maximum

- **Difficulty**: Hard
- **Category**: Sliding Window
- **Topics**: array, sliding window, monotonic deque
- **Link**: [NeetCode](https://neetcode.io/problems/sliding-window-maximum) | [LeetCode 239](https://leetcode.com/problems/sliding-window-maximum/)

## Description

You are given an array of integers `nums`, and there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max value in each sliding window position.

## Examples

**Example 1:**

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7      3
 1 [3  -1  -3] 5  3  6  7      3
 1  3 [-1  -3  5] 3  6  7      5
 1  3  -1 [-3  5  3] 6  7      5
 1  3  -1  -3 [5  3  6] 7      6
 1  3  -1  -3  5 [3  6  7]     7
```

**Example 2:**

```
Input: nums = [1,3,2], k = 3
Output: [3]
Explanation: There is only one window of size 3, and its maximum is 3.
```

**Example 3:**

```
Input: nums = [1,-1,3], k = 1
Output: [1,-1,3]
Explanation: When k = 1, each element is its own window, so the output is the array itself.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Function Signature

**Go:**

```go
func maxSlidingWindow(nums []int, k int) []int
```

**Python:**
```python
def max_sliding_window(nums: List[int], k: int) -> List[int]:
```
