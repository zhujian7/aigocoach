# Copy List with Random Pointer

- **Difficulty**: Medium
- **Category**: Linked List
- **Topics**: linked list, hash map, deep copy
- **Link**: [NeetCode](https://neetcode.io/problems/copy-linked-list-with-random-pointer) | [LeetCode 138](https://leetcode.com/problems/copy-list-with-random-pointer/)

## Description

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

## Examples

**Example 1:**

![Example 1](assets/e1.png)

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Explanation: Each pair [val, random_index] describes a node. The deep copy preserves the same structure.
```

**Example 2:**

![Example 2](assets/e2.png)

```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Explanation: Node 0's random points to node 1, and node 1's random also points to node 1.
```

**Example 3:**

![Example 3](assets/e3.png)

```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Explanation: Nodes can have the same values. Random pointers can be null.
```

## Constraints

- `0 <= n <= 1000`
- `-10^4 <= Node.Val <= 10^4`
- `Node.Random` is `null` or is pointing to some node in the linked list

## Function Signature

**Go:**

```go
func copyRandomList(head *RandomNode) *RandomNode
```

**Python:**
```python
class RandomNode
def __init__(self, val: int = 0, next: 'RandomNode' = None, random: 'RandomNode' = None):
def copy_random_list(head: Optional[RandomNode]) -> Optional[RandomNode]:
```
