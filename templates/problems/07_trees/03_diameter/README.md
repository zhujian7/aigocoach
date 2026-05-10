# Diameter of Binary Tree

- **Difficulty**: Easy
- **Category**: Trees
- **Topics**: binary tree, DFS, recursion
- **Link**: [NeetCode](https://neetcode.io/problems/binary-tree-diameter) | [LeetCode 543](https://leetcode.com/problems/diameter-of-binary-tree/)

## Description

![diameter-of-binary-tree](assets/diamtree.jpg)

Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root. The length of a path is measured by the number of edges between nodes.

## Examples

**Example 1:**

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: The longest path is 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3, which has 3 edges.
```

**Example 2:**

```
Input: root = [1,2]
Output: 1
Explanation: The only path is between node 1 and node 2, which has 1 edge.
```

**Example 3:**

```
Input: root = [1]
Output: 0
Explanation: A single node has no edges, so the diameter is 0.
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

## Function Signature

**Go:**

```go
func diameterOfBinaryTree(root *TreeNode) int
```

**Python:**
```python
def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
```
