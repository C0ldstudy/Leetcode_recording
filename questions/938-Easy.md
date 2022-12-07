### 938. Range Sum of BST

Given the `root` node of a binary search tree and two integers `low` and `high`, return the sum of values of all nodes with a value in the inclusive range `[low, high]`.



### Key insight
- use a deep first search to check each node meeting the requirement.



### Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = self.dfs(root, low, high)
        return result

    def dfs(self, node, low, high):
        result = 0
        if node:
            if low<= node.val <= high:
                result += node.val
            if low < node.val:
                result += self.dfs(node.left, low, high)
            if high > node.val:
                result += self.dfs(node.right, low, high)
        return result
```
