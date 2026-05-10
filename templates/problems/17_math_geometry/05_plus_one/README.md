# Plus One

- **Difficulty**: Easy
- **Category**: Math & Geometry
- **Topics**: array, math
- **Link**: [NeetCode](https://neetcode.io/problems/plus-one) | [LeetCode 66](https://leetcode.com/problems/plus-one/)

## Description

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i`-th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

## Examples

**Example 1:**

```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123. Incrementing by one gives 124.
```

**Example 2:**

```
Input: digits = [4,3,2,9]
Output: [4,3,3,0]
Explanation: The array represents the integer 4329. Incrementing by one gives 4330.
```

**Example 3:**

```
Input: digits = [9,9,9]
Output: [1,0,0,0]
Explanation: The array represents the integer 999. Incrementing by one gives 1000, which requires an additional digit.
```

## Constraints

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading `0`'s

## Function Signature

**Go:**

```go
func plusOne(digits []int) []int
```

**Python:**
```python
def plus_one(digits: List[int]) -> List[int]:
```
