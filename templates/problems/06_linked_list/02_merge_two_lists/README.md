# Merge Two Sorted Lists

- **Difficulty**: Easy
- **Category**: Linked List
- **Topics**: linked list, recursion, iteration
- **Link**: [NeetCode](https://neetcode.io/problems/merge-two-sorted-linked-lists) | [LeetCode 21](https://leetcode.com/problems/merge-two-sorted-lists/)

## Description

![merge-two-sorted-lists](assets/merge_ex1.jpg)

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Examples

**Example 1:**

```
Input: list1 = [1,3,5], list2 = [2,4,6]
Output: [1,2,3,4,5,6]
Explanation: The two sorted lists are interleaved into one sorted list.
```

**Example 2:**

```
Input: list1 = [], list2 = [1,2,3]
Output: [1,2,3]
Explanation: When one list is empty, the result is the other list.
```

**Example 3:**

```
Input: list1 = [], list2 = []
Output: []
Explanation: Merging two empty lists produces an empty list.
```

## Constraints

- The number of nodes in both lists is in the range `[0, 50]`
- `-100 <= Node.Val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order

## Function Signature

**Go:**

```go
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode
```

**Python:**
```python
def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
```
