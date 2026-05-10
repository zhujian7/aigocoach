# Missing Number

- **Difficulty**: Easy
- **Category**: Bit Manipulation
- **Topics**: array, bit manipulation, math, XOR
- **Link**: [NeetCode](https://neetcode.io/problems/missing-number) | [LeetCode 268](https://leetcode.com/problems/missing-number/)

## Description

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

You should implement a solution that uses only `O(1)` extra space and runs in `O(n)` time.

## Examples

**Example 1:**

```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number.
```

**Example 2:**

```
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number.
```

**Example 3:**

```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number.
```

## Constraints

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All the numbers of `nums` are unique

## Function Signature

**Go:**

```go
func missingNumber(nums []int) int
```

**Python:**
```python
def missing_number(nums: List[int]) -> int:
```
