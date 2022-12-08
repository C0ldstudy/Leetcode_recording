### 872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



### Solution
```python
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # seq = []
        def bfs(root):
            seq = []
            if (not root.left) and (not root.right): return str(root.val)
            left_result, right_result = '', ''

            if root.left:
                left_result = bfs(root.left)
            elif root.right:
                right_result = bfs(root.right)
                return str(right_result)
            else:
                return
            if root.right:
                right_result = bfs(root.right)
                return str(left_result)+','+str(right_result)
            else:
                return str(left_result)
        seq1 = bfs(root1)
        seq2 = bfs(root2)
        if seq1 == seq2:
            return True
        else:
            return False
```

The simpler one. `yield` is the function I learned this time.
```python
class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
        seq1 = list(dfs(root1))
        seq2 = list(dfs(root2))
        print(seq1, seq2)
        if seq1 == seq2:
            return True
        else:
            return False
```
