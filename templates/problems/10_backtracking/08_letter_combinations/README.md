# Letter Combinations of a Phone Number

- **Difficulty**: Medium
- **Category**: Backtracking
- **Topics**: backtracking, string, hash map
- **Link**: [NeetCode](https://neetcode.io/problems/letter-combinations-of-a-phone-number) | [LeetCode 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## Description

![letter-combinations-of-a-phone-number](assets/1200px-telephone-keypad2svg.png)

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

The mapping of digits to letters is the same as on a telephone keypad: 2 maps to "abc", 3 to "def", 4 to "ghi", 5 to "jkl", 6 to "mno", 7 to "pqrs", 8 to "tuv", and 9 to "wxyz". Note that digit 1 does not map to any letters.

## Examples

**Example 1:**

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Example 2:**

```
Input: digits = ""
Output: []
```

**Example 3:**

```
Input: digits = "2"
Output: ["a","b","c"]
```

## Constraints

- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

## Function Signature

**Go:**

```go
func letterCombinations(digits string) []string
```

**Python:**
```python
def letter_combinations(digits: str) -> List[str]:
```
