# Kth Smallest Element in a BST

- **Difficulty**: Medium
- **Category**: Trees
- **Topics**: binary search tree, inorder traversal, DFS
- **Link**: [NeetCode](https://neetcode.io/problems/kth-smallest-integer-in-bst) | [LeetCode 230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## Description

Given the root of a binary search tree and an integer `k`, return the `k`th smallest value (1-indexed) among all the values of the nodes in the tree. Since the BST property guarantees that an inorder traversal yields values in ascending order, the `k`th element visited during inorder traversal is the answer.

## Examples

**Example 1:**

![Example 1](assets/kthtree1.jpg)

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
Explanation: The inorder traversal is [1, 2, 3, 4]. The 1st smallest element is 1.
```

**Example 2:**

![Example 2](assets/kthtree2.jpg)

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
Explanation: The inorder traversal is [1, 2, 3, 4, 5, 6]. The 3rd smallest element is 3.
```

**Example 3:**

```
Input: root = [3,1,4,null,2], k = 2
Output: 2
Explanation: The inorder traversal is [1, 2, 3, 4]. The 2nd smallest element is 2.
```

## Constraints

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

## Function Signature

**Go:**

```go
func kthSmallest(root *TreeNode, k int) int
```

**Python:**
```python
def kth_smallest(root: Optional[TreeNode], k: int) -> int:
```
