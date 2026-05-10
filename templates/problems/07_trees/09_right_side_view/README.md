# Binary Tree Right Side View

- **Difficulty**: Medium
- **Category**: Trees
- **Topics**: binary tree, BFS, queue
- **Link**: [NeetCode](https://neetcode.io/problems/binary-tree-right-side-view) | [LeetCode 199](https://leetcode.com/problems/binary-tree-right-side-view/)

## Description

Given the root of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see ordered from top to bottom. For each level of the tree, only the rightmost node is visible from the right side.

## Examples

**Example 1:**

![Example 1](assets/tmpd5jn43fs-1.png)

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation: At level 0 you see node 1, at level 1 you see node 3 (rightmost), at level 2 you see node 4 (rightmost).
```

**Example 2:**

![Example 2](assets/tmpkpe40xeh-1.png)

```
Input: root = [1,null,3]
Output: [1,3]
Explanation: At level 0 you see node 1, at level 1 you see node 3.
```

**Example 3:**

```
Input: root = [1,2,3,4]
Output: [1,3,4]
Explanation: At level 0 you see 1, at level 1 node 3 is rightmost, at level 2 node 4 is the only node (left child of 2) and is visible from the right.
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Function Signature

**Go:**

```go
func rightSideView(root *TreeNode) []int
```

**Python:**
```python
def right_side_view(root: Optional[TreeNode]) -> List[int]:
```
