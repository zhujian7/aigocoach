# Evaluate Reverse Polish Notation

- **Difficulty**: Medium
- **Category**: Stack
- **Topics**: stack, math, string
- **Link**: [NeetCode](https://neetcode.io/problems/evaluate-reverse-polish-notation) | [LeetCode 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

## Description

You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation (postfix notation). Evaluate the expression and return an integer that represents the value of the expression.

Note that:
- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

## Examples

**Example 1:**

```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:**

```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Example 3:**

```
Input: tokens = ["1","2","-"]
Output: -1
Explanation: (1 - 2) = -1
```

## Constraints

- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator `"+"`, `"-"`, `"*"`, `"/"`, or an integer in the range `[-200, 200]`

## Function Signature

**Go:**

```go
func evalRPN(tokens []string) int
```

**Python:**
```python
def eval_rpn(tokens: List[str]) -> int:
```
