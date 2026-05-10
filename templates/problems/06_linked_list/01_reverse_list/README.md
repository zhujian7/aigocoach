# Reverse Linked List

- **Difficulty**: Easy
- **Category**: Linked List
- **Topics**: linked list, iteration
- **Link**: [NeetCode](https://neetcode.io/problems/reverse-a-linked-list) | [LeetCode 206](https://leetcode.com/problems/reverse-linked-list/)

## Description

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

Each node in the linked list contains a single integer value and a pointer to the next node. After reversal, the last node becomes the first node, and all pointers are reversed so the list is traversed in the opposite direction.

## Examples

**Example 1:**

![Example 1](assets/rev1ex1.jpg)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Explanation: The list 1->2->3->4->5 becomes 5->4->3->2->1.
```

**Example 2:**

![Example 2](assets/rev1ex2.jpg)

```
Input: head = [1,2]
Output: [2,1]
Explanation: The list 1->2 becomes 2->1.
```

**Example 3:**

```
Input: head = []
Output: []
Explanation: An empty list remains empty after reversal.
```

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`
- `-5000 <= Node.Val <= 5000`

## Function Signature

**Go:**

```go
func reverseList(head *ListNode) *ListNode
```

**Python:**
```python
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
```
