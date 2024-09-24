# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if (not root.left) and (not root.right):
            return True
        elif root.left and root.right:
            return self.check(root.left, root.right)
        else:
            return False
    
    def check(self, n1, n2):
        if (not n1) and n2: return False
        if (not n2) and n1: return False
        if (not n1) and (not n2): return True
        
        if n1.val != n2.val: return False            
        if not self.check(n1.left, n2.right): return False
        if not self.check(n1.right, n2.left): return False
        return True
                
                
            
            