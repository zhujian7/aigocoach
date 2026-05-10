# Reverse Bits

- **Difficulty**: Easy
- **Category**: Bit Manipulation
- **Topics**: bit manipulation
- **Link**: [NeetCode](https://neetcode.io/problems/reverse-bits) | [LeetCode 190](https://leetcode.com/problems/reverse-bits/)

## Description

Reverse the bits of a given 32-bit unsigned integer. For example, if the input binary representation is `00000010100101000001111010011100`, the output should be `00111001011110000010100101000000`, which corresponds to the unsigned integer `964176192`.

## Examples

**Example 1:**

```
Input: n = 00000010100101000001111010011100
Output: 964176192 (00111001011110000010100101000000)
Explanation: The input represents the unsigned integer 43261596. Reversing its bits gives 964176192.
```

**Example 2:**

```
Input: n = 11111111111111111111111111111101
Output: 3221225471 (10111111111111111111111111111111)
Explanation: The input represents the unsigned integer 4294967293. Reversing its bits gives 3221225471.
```

**Example 3:**

```
Input: n = 1
Output: 2147483648 (10000000000000000000000000000000)
Explanation: Reversing the bits of 1 places the single set bit at position 31.
```

## Constraints

- The input must be a binary string of length `32`

## Function Signature

**Go:**

```go
func reverseBits(num uint32) uint32
```

**Python:**
```python
def reverse_bits(num: int) -> int:
```
