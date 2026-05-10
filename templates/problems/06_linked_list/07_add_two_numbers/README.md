# Add Two Numbers

- **Difficulty**: Medium
- **Category**: Linked List
- **Topics**: linked list, math, simulation
- **Link**: [NeetCode](https://neetcode.io/problems/add-two-numbers) | [LeetCode 2](https://leetcode.com/problems/add-two-numbers/)

## Description

![add-two-numbers](assets/addtwonumber1.jpg)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Examples

**Example 1:**

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807, represented in reverse as [7,0,8].
```

**Example 2:**

```
Input: l1 = [0], l2 = [0]
Output: [0]
Explanation: 0 + 0 = 0.
```

**Example 3:**

```
Input: l1 = [9,9,9], l2 = [1]
Output: [0,0,0,1]
Explanation: 999 + 1 = 1000, represented in reverse as [0,0,0,1].
```

## Constraints

- The number of nodes in each linked list is in the range `[1, 100]`
- `0 <= Node.Val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros

## Function Signature

**Go:**

```go
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode
```

**Python:**
```python
def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
```
