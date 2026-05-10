# Counting Bits

- **Difficulty**: Easy
- **Category**: Bit Manipulation
- **Topics**: bit manipulation, dynamic programming
- **Link**: [NeetCode](https://neetcode.io/problems/counting-bits) | [LeetCode 338](https://leetcode.com/problems/counting-bits/)

## Description

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the number of `1`'s in the binary representation of `i`.

You should find a solution that runs in `O(n)` time without using the built-in popcount function for each number.

## Examples

**Example 1:**

```
Input: n = 2
Output: [0,1,1]
Explanation: 0 -> 0 (zero 1's), 1 -> 1 (one 1), 2 -> 10 (one 1).
```

**Example 2:**

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation: 0->0, 1->1, 2->10, 3->11, 4->100, 5->101.
```

**Example 3:**

```
Input: n = 0
Output: [0]
Explanation: Only 0 itself, which has zero 1 bits.
```

## Constraints

- `0 <= n <= 10^5`

## Function Signature

**Go:**

```go
func countBits(n int) []int
```

**Python:**
```python
def count_bits(n: int) -> List[int]:
```
