# Serialize and Deserialize Binary Tree

- **Difficulty**: Hard
- **Category**: Trees
- **Topics**: binary tree, preorder traversal, string processing
- **Link**: [NeetCode](https://neetcode.io/problems/serialize-and-deserialize-binary-tree) | [LeetCode 297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

## Description

![serialize-and-deserialize-binary-tree](assets/serdeser.jpg)

Design an algorithm to serialize and deserialize a binary tree. Serialization is the process of converting a tree into a string representation so that it can be stored or transmitted, and deserialization is the process of reconstructing the tree from the string. There is no restriction on how your serialization/deserialization algorithm should work, as long as a binary tree can be serialized to a string and this string can be deserialized back to the original tree structure.

## Examples

**Example 1:**

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Explanation: The tree is serialized to a string, then deserialized back to produce an identical tree.
```

**Example 2:**

```
Input: root = []
Output: []
Explanation: An empty tree serializes and deserializes as empty.
```

**Example 3:**

```
Input: root = [1]
Output: [1]
Explanation: A single node tree is preserved through serialization and deserialization.
```

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-1000 <= Node.val <= 1000`

## Function Signature

**Go:**

```go
func serialize(root *TreeNode) string

func deserialize(data string) *TreeNode
```

**Python:**
```python
def serialize(root: Optional[TreeNode]) -> str:
def deserialize(data: str) -> Optional[TreeNode]:
```
