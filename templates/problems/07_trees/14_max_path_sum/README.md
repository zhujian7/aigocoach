# Binary Tree Maximum Path Sum

- **Difficulty**: Hard
- **Category**: Trees
- **Topics**: binary tree, DFS, dynamic programming on trees
- **Link**: [NeetCode](https://neetcode.io/problems/binary-tree-maximum-path-sum) | [LeetCode 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

## Description

Given the root of a binary tree, return the maximum path sum of any non-empty path. A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. The path does not need to pass through the root, and it can start and end at any node in the tree. Node values can be negative.

## Examples

**Example 1:**

![Example 1](assets/exx1.jpg)

```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

**Example 2:**

![Example 2](assets/exx2.jpg)

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

**Example 3:**

```
Input: root = [-3]
Output: -3
Explanation: With only one node, the maximum path sum is the node's value itself.
```

## Constraints

- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
- `-1000 <= Node.val <= 1000`

## Function Signature

**Go:**

```go
func maxPathSum(root *TreeNode) int
```

**Python:**
```python
def max_path_sum(root: Optional[TreeNode]) -> int:
```
