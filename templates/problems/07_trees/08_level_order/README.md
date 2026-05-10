# Binary Tree Level Order Traversal

- **Difficulty**: Medium
- **Category**: Trees
- **Topics**: binary tree, BFS, queue
- **Link**: [NeetCode](https://neetcode.io/problems/level-order-traversal-of-binary-tree) | [LeetCode 102](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## Description

![binary-tree-level-order-traversal](assets/tree1.jpg)

Given the root of a binary tree, return the level order traversal of its nodes' values. Level order traversal processes nodes from left to right, level by level, starting from the root. The result is a list of lists, where each inner list contains the values of nodes at the corresponding depth level.

## Examples

**Example 1:**

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Explanation: Level 0 has node 3, level 1 has nodes 9 and 20, level 2 has nodes 15 and 7.
```

**Example 2:**

```
Input: root = [1]
Output: [[1]]
Explanation: The tree has only one node at level 0.
```

**Example 3:**

```
Input: root = []
Output: []
Explanation: An empty tree produces an empty result.
```

## Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

## Function Signature

**Go:**

```go
func levelOrder(root *TreeNode) [][]int
```

**Python:**
```python
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
```
