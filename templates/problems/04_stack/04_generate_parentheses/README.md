# Generate Parentheses

- **Difficulty**: Medium
- **Category**: Stack
- **Topics**: backtracking, string, recursion
- **Link**: [NeetCode](https://neetcode.io/problems/generate-parentheses) | [LeetCode 22](https://leetcode.com/problems/generate-parentheses/)

## Description

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

A combination of parentheses is well-formed if every opening parenthesis `'('` has a corresponding closing parenthesis `')'` and the pairs are properly nested.

## Examples

**Example 1:**

```
Input: n = 1
Output: ["()"]
```

**Example 2:**

```
Input: n = 2
Output: ["(())","()()"]
```

**Example 3:**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Explanation: All 5 possible combinations of 3 pairs of well-formed parentheses.
```

## Constraints

- `1 <= n <= 8`

## Function Signature

**Go:**

```go
func generateParenthesis(n int) []string
```

**Python:**
```python
def generate_parenthesis(n: int) -> List[str]:
```
