# Remove Nth Node From End of List

- **Difficulty**: Medium
- **Category**: Linked List
- **Topics**: linked list, two pointers
- **Link**: [NeetCode](https://neetcode.io/problems/remove-node-from-end-of-linked-list) | [LeetCode 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## Description

![remove-nth-node-from-end-of-list](assets/remove_ex1.jpg)

Given the `head` of a linked list, remove the `n`th node from the end of the list and return its head.

The problem guarantees that `n` is always valid -- that is, `n` will always be less than or equal to the length of the list.

## Examples

**Example 1:**

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Explanation: The 2nd node from the end is node 4, so it is removed.
```

**Example 2:**

```
Input: head = [1], n = 1
Output: []
Explanation: The only node is removed, resulting in an empty list.
```

**Example 3:**

```
Input: head = [1,2], n = 1
Output: [1]
Explanation: The last node (value 2) is removed.
```

## Constraints

- The number of nodes in the list is `sz`
- `1 <= sz <= 30`
- `0 <= Node.Val <= 100`
- `1 <= n <= sz`

## Function Signature

**Go:**

```go
func removeNthFromEnd(head *ListNode, n int) *ListNode
```

**Python:**
```python
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
```
