# Valid Palindrome

- **Difficulty**: Easy
- **Category**: Two Pointers
- **Topics**: string, two pointers
- **Link**: [NeetCode](https://neetcode.io/problems/is-palindrome) | [LeetCode 125](https://leetcode.com/problems/valid-palindrome/)

## Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples

**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: After removing non-alphanumeric characters and converting to lowercase, "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**

```
Input: s = "race a car"
Output: false
Explanation: After processing, "raceacar" is not a palindrome.
```

**Example 3:**

```
Input: s = " "
Output: true
Explanation: After removing non-alphanumeric characters, s is an empty string "". An empty string reads the same forward and backward, so it is a palindrome.
```

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Function Signature

**Go:**

```go
func isPalindrome(s string) bool
```

**Python:**
```python
def is_palindrome(s: str) -> bool:
```
