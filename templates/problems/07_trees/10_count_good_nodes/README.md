# Count Good Nodes in Binary Tree

- **Difficulty**: Medium
- **Category**: Trees
- **Topics**: binary tree, DFS, recursion
- **Link**: [NeetCode](https://neetcode.io/problems/count-good-nodes-in-binary-tree) | [LeetCode 1448](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

## Description

Given a binary tree `root`, a node X in the tree is named "good" if in the path from root to X there are no nodes with a value greater than X. Return the number of good nodes in the binary tree. The root is always considered a good node.

## Examples

**Example 1:**

![Example 1](assets/test_sample_1.png)

```
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: The good nodes are: root node 3, node 3 (left-left, path max is 3), node 4 (right, 4 >= 3), and node 5 (right-right, 5 >= 4). Node 1 (left) is not good because 3 > 1.
```

**Example 2:**

![Example 2](assets/test_sample_2.png)

```
Input: root = [3,3,null,4,2]
Output: 3
Explanation: The good nodes are: root 3, node 3 (left, 3 >= 3), and node 4 (left-left, 4 >= 3). Node 2 is not good because 3 > 2.
```

**Example 3:**

```
Input: root = [1]
Output: 1
Explanation: The root is always a good node.
```

## Constraints

- The number of nodes in the binary tree is in the range `[1, 10^5]`.
- Each node's value is between `[-10^4, 10^4]`.

## Function Signature

**Go:**

```go
func goodNodes(root *TreeNode) int
```

**Python:**
```python
def good_nodes(root: Optional[TreeNode]) -> int:
```
