# Subtree of Another Tree

- **Difficulty**: Easy
- **Category**: Trees
- **Topics**: binary tree, DFS, recursion
- **Link**: [NeetCode](https://neetcode.io/problems/subtree-of-a-binary-tree) | [LeetCode 572](https://leetcode.com/problems/subtree-of-another-tree/)

## Description

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values as `subRoot`. A subtree of a binary tree is a tree that consists of a node in the tree and all of this node's descendants. The tree could also be considered as a subtree of itself.

## Examples

**Example 1:**

![Example 1](assets/subtree1-tree.jpg)

```
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Explanation: The subtree rooted at node 4 in root matches subRoot exactly.
```

**Example 2:**

![Example 2](assets/subtree2-tree.jpg)

```
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
Explanation: The subtree rooted at node 4 has an extra child (0) under node 2, so it does not match subRoot.
```

**Example 3:**

```
Input: root = [1], subRoot = [1]
Output: true
Explanation: The entire tree is identical to subRoot.
```

## Constraints

- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

## Function Signature

**Go:**

```go
func isSubtree(root *TreeNode, subRoot *TreeNode) bool
```

**Python:**
```python
def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
```
