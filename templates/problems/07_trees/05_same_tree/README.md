# Same Tree

- **Difficulty**: Easy
- **Category**: Trees
- **Topics**: binary tree, DFS, recursion
- **Link**: [NeetCode](https://neetcode.io/problems/same-binary-tree) | [LeetCode 100](https://leetcode.com/problems/same-tree/)

## Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same values at every corresponding position.

## Examples

**Example 1:**

![Example 1](assets/ex1.jpg)

```
Input: p = [1,2,3], q = [1,2,3]
Output: true
Explanation: Both trees have the same structure and same node values.
```

**Example 2:**

![Example 2](assets/ex2.jpg)

```
Input: p = [1,2], q = [1,null,2]
Output: false
Explanation: The first tree has 2 as a left child, but the second tree has 2 as a right child. They are structurally different.
```

**Example 3:**

![Example 3](assets/ex3.jpg)

```
Input: p = [1,2,1], q = [1,1,2]
Output: false
Explanation: Both trees have the same structure but different values at corresponding positions.
```

## Constraints

- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

## Function Signature

**Go:**

```go
func isSameTree(p *TreeNode, q *TreeNode) bool
```

**Python:**
```python
def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
```
