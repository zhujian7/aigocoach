# Min Stack

- **Difficulty**: Medium
- **Category**: Stack
- **Topics**: stack, design
- **Link**: [NeetCode](https://neetcode.io/problems/minimum-stack) | [LeetCode 155](https://leetcode.com/problems/min-stack/)

## Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `Push(val int)` pushes the element `val` onto the stack.
- `Pop()` removes the element on the top of the stack.
- `Top() int` gets the top element of the stack.
- `GetMin() int` retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

## Examples

**Example 1:**

```
Input:
["MinStack","Push","Push","Push","GetMin","Pop","Top","GetMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output:
[null,null,null,null,-3,null,0,-2]
Explanation:
MinStack minStack = new MinStack();
minStack.Push(-2);
minStack.Push(0);
minStack.Push(-3);
minStack.GetMin(); // return -3
minStack.Pop();
minStack.Top();    // return 0
minStack.GetMin(); // return -2
```

**Example 2:**

```
Input:
["MinStack","Push","Top","GetMin"]
[[],[5],[],[]]
Output:
[null,null,5,5]
Explanation: After pushing 5, both Top and GetMin return 5.
```

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- Methods `Pop`, `Top` and `GetMin` will always be called on non-empty stacks
- At most `3 * 10^4` calls will be made to `Push`, `Pop`, `Top`, and `GetMin`

## Function Signature

**Go:**

```go
type MinStack struct{}

func NewMinStack() MinStack
func (s *MinStack) Push(val int)
func (s *MinStack) Pop()
func (s *MinStack) Top() int
func (s *MinStack) GetMin() int
```

**Python:**
```python
class MinStack
def __init__(self):
def push(self, val: int) -> None:
def pop(self) -> None:
def top(self) -> int:
def get_min(self) -> int:
```
