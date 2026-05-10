# Maximum Product Subarray

- **Difficulty**: Medium
- **Category**: 1D Dynamic Programming
- **Topics**: dynamic programming, array
- **Link**: [NeetCode](https://neetcode.io/problems/maximum-product-subarray) | [LeetCode 152](https://leetcode.com/problems/maximum-product-subarray/)

## Description

Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product. The array may contain positive numbers, negative numbers, and zeros. The test cases are generated so that the answer will fit in a 32-bit integer.

## Examples

**Example 1:**

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: The subarray [2,3] has the largest product 6.
```

**Example 2:**

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2 because [-2,-1] is not a contiguous subarray.
```

**Example 3:**

```
Input: nums = [-2,-3]
Output: 6
Explanation: The subarray [-2,-3] has the product 6.
```

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is guaranteed to fit in a 32-bit integer.

## Function Signature

**Go:**

```go
func maxProduct(nums []int) int
```

**Python:**
```python
def max_product(nums: List[int]) -> int:
```
