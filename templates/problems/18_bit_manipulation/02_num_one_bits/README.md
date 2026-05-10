# Number of 1 Bits

- **Difficulty**: Easy
- **Category**: Bit Manipulation
- **Topics**: bit manipulation
- **Link**: [NeetCode](https://neetcode.io/problems/number-of-one-bits) | [LeetCode 191](https://leetcode.com/problems/number-of-1-bits/)

## Description

Write a function that takes the binary representation of a positive integer and returns the number of set bits (1 bits) it has, also known as the Hamming weight.

## Examples

**Example 1:**

```
Input: n = 11 (binary: 00000000000000000000000000001011)
Output: 3
Explanation: The binary representation has three 1 bits.
```

**Example 2:**

```
Input: n = 128 (binary: 00000000000000000000000010000000)
Output: 1
Explanation: The binary representation has one 1 bit.
```

**Example 3:**

```
Input: n = 4294967293 (binary: 11111111111111111111111111111101)
Output: 31
Explanation: The binary representation has thirty-one 1 bits.
```

## Constraints

- The input is a 32-bit unsigned integer

## Function Signature

**Go:**

```go
func hammingWeight(n uint32) int
```

**Python:**
```python
def hamming_weight(n: int) -> int:
```
