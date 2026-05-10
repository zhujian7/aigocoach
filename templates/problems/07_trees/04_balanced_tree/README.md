# Balanced Binary Tree

- **Difficulty**: Easy
- **Category**: Trees
- **Topics**: binary tree, DFS, recursion
- **Link**: [NeetCode](https://neetcode.io/problems/balanced-binary-tree) | [LeetCode 110](https://leetcode.com/problems/balanced-binary-tree/)

## Description

Given a binary tree, determine if it is height-balanced. A binary tree is height-balanced if for every node in the tree, the difference between the heights of its left subtree and right subtree is at most 1.

## Examples

**Example 1:**

![Example 1](assets/balance_1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: true
Explanation: The left subtree has height 1, the right subtree has height 2. The difference is 1, which satisfies the balanced condition at every node.
```

**Example 2:**

![Example 2](assets/balance_2.jpg)

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Explanation: The left subtree of the root has height 3, while the right subtree has height 1. The difference is 2, so the tree is not balanced.
```

**Example 3:**

```
Input: root = []
Output: true
Explanation: An empty tree is considered balanced.
```

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

## Function Signature

**Go:**

```go
func isBalanced(root *TreeNode) bool
```

**Python:**
```python
def is_balanced(root: Optional[TreeNode]) -> bool:
```
