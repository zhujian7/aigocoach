# Construct Binary Tree from Preorder and Inorder Traversal

- **Difficulty**: Medium
- **Category**: Trees
- **Topics**: binary tree, recursion, hash map, divide and conquer
- **Link**: [NeetCode](https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal) | [LeetCode 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## Description

![construct-binary-tree-from-preorder-and-inorder-traversal](assets/tree.jpg)

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree. It is guaranteed that the values are unique and both arrays have the same length.

## Examples

**Example 1:**

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Explanation: The root is 3 (first element of preorder). In inorder, 9 is to the left of 3 (left subtree) and [15,20,7] is to the right (right subtree).
```

**Example 2:**

```
Input: preorder = [1], inorder = [1]
Output: [1]
Explanation: A single node tree.
```

**Example 3:**

```
Input: preorder = [1,2], inorder = [2,1]
Output: [1,2]
Explanation: Node 2 appears before 1 in inorder, so 2 is the left child of 1.
```

## Constraints

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of unique values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is guaranteed to be the preorder traversal and `inorder` the inorder traversal of the same tree.

## Function Signature

**Go:**

```go
func buildTreeFromPreIn(preorder []int, inorder []int) *TreeNode
```

**Python:**
```python
def build_tree_from_pre_in(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
```
