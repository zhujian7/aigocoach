# Merge K Sorted Lists

- **Difficulty**: Hard
- **Category**: Linked List
- **Topics**: linked list, heap, divide and conquer
- **Link**: [NeetCode](https://neetcode.io/problems/merge-k-sorted-linked-lists) | [LeetCode 23](https://leetcode.com/problems/merge-k-sorted-lists/)

## Description

You are given an array of `k` linked lists `lists`, each linked list is sorted in ascending order. Merge all the linked lists into one sorted linked list and return it.

## Examples

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The three sorted linked lists are merged into one sorted list by comparing heads and always picking the smallest.
```

**Example 2:**

```
Input: lists = []
Output: []
Explanation: An empty array of lists produces an empty result.
```

**Example 3:**

```
Input: lists = [[]]
Output: []
Explanation: A single empty list results in an empty merged list.
```

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order
- The sum of `lists[i].length` will not exceed `10^4`

## Function Signature

**Go:**

```go
func mergeKLists(lists []*ListNode) *ListNode
```

**Python:**
```python
def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
```
