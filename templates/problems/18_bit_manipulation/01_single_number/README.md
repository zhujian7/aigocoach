# Single Number

- **Difficulty**: Easy
- **Category**: Bit Manipulation
- **Topics**: array, bit manipulation, XOR
- **Link**: [NeetCode](https://neetcode.io/problems/single-number) | [LeetCode 136](https://leetcode.com/problems/single-number/)

## Description

Given a non-empty array of integers `nums`, every element appears exactly twice except for one element which appears exactly once. Find that single element.

You must implement a solution with linear runtime complexity and use only constant extra space.

## Examples

**Example 1:**

```
Input: nums = [2,2,1]
Output: 1
Explanation: 1 is the only element that appears once.
```

**Example 2:**

```
Input: nums = [4,1,2,1,2]
Output: 4
Explanation: 4 is the only element that appears once; 1 and 2 each appear twice.
```

**Example 3:**

```
Input: nums = [1]
Output: 1
Explanation: There is only one element, so it is the single number.
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Each element in the array appears exactly twice except for one element which appears exactly once

## Function Signature

**Go:**

```go
func singleNumber(nums []int) int
```

**Python:**
```python
def single_number(nums: List[int]) -> int:
```
