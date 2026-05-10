# Reverse Nodes in K-Group

- **Difficulty**: Hard
- **Category**: Linked List
- **Topics**: linked list, recursion, iteration
- **Link**: [NeetCode](https://neetcode.io/problems/reverse-nodes-in-k-group) | [LeetCode 25](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Description

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

## Examples

**Example 1:**

![Example 1](assets/reverse_ex1.jpg)

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Explanation: Nodes are reversed in groups of 2. The last node (5) has no complete group, so it stays.
```

**Example 2:**

![Example 2](assets/reverse_ex2.jpg)

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Explanation: Only the first 3 nodes are reversed. The remaining 2 nodes stay in original order.
```

**Example 3:**

```
Input: head = [1,2,3,4], k = 2
Output: [2,1,4,3]
Explanation: Two complete groups of 2 are each reversed.
```

## Constraints

- The number of nodes in the list is `n`
- `1 <= k <= n <= 5000`
- `0 <= Node.Val <= 1000`

## Function Signature

**Go:**

```go
func reverseKGroup(head *ListNode, k int) *ListNode
```

**Python:**
```python
def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
```
