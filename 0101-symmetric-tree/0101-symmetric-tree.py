# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res = True
        if (not root.left) and (not root.right):
            return True
        elif (not root.left) or (not root.right):
            return False
        else:
            res = self.check(root.left, root.right, res)
        return res
    
    def check(self, left, right, res):
        if left==None and right==None:
            return res
        elif left==None or right==None:
            return False
        if not self.check(left.left, right.right, res): return False
        if left.val != right.val: return False
        if not self.check(left.right, right.left, res): return False
        return True
        
        
        