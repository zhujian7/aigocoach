# Validate Binary Search Tree

- **Difficulty**: Medium
- **Category**: Trees
- **Topics**: binary search tree, DFS, recursion
- **Link**: [NeetCode](https://neetcode.io/problems/valid-binary-search-tree) | [LeetCode 98](https://leetcode.com/problems/validate-binary-search-tree/)

## Description

Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows: the left subtree of a node contains only nodes with keys strictly less than the node's key, the right subtree contains only nodes with keys strictly greater than the node's key, and both the left and right subtrees must also be valid binary search trees.

## Examples

**Example 1:**

![Example 1](assets/tree1.jpg)

```
Input: root = [2,1,3]
Output: true
Explanation: Node 1 < 2 (valid left child) and node 3 > 2 (valid right child).
```

**Example 2:**

![Example 2](assets/tree2.jpg)

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5, but its right child is 4, which is less than 5. This violates the BST property.
```

**Example 3:**

```
Input: root = [5,4,6,null,null,3,7]
Output: false
Explanation: Node 3 is in the right subtree of root 5 but has value 3, which is less than 5. Even though 3 < 6 (its parent), it violates the BST constraint relative to the root.
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Function Signature

**Go:**

```go
func isValidBST(root *TreeNode) bool
```

**Python:**
```python
def is_valid_bst(root: Optional[TreeNode]) -> bool:
```
