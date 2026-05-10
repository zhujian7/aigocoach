# Product of Array Except Self

- **Difficulty**: Medium
- **Category**: Arrays & Hashing
- **Topics**: array, prefix sum
- **Link**: [NeetCode](https://neetcode.io/problems/products-of-array-discluding-self) | [LeetCode 238](https://leetcode.com/problems/product-of-array-except-self/)

## Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

## Examples

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: For index 0: 2*3*4=24, index 1: 1*3*4=12, index 2: 1*2*4=8, index 3: 1*2*3=6.
```

**Example 2:**

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Explanation: The element at index 2 is 0, so all products except that position become 0. For index 2: (-1)*1*(-3)*3 = 9.
```

**Example 3:**

```
Input: nums = [2,3]
Output: [3,2]
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

## Function Signature

**Go:**

```go
func productExceptSelf(nums []int) []int
```

**Python:**
```python
def product_except_self(nums: List[int]) -> List[int]:
```
