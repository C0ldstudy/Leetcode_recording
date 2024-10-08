# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root != None:
            left = self.inorderTraversal(root.left)
            right = self.inorderTraversal(root.right)
            res = left + [root.val] + right
        return res