# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        res = self.traversal(p, q, res)
        return res
    def traversal(self, p, q, res):
        if (p == None) and (q == None): 
            return res
        elif (p == None) or (q == None):
            return False
        if not self.traversal(p.left,q.left, res): return False
        if p.val != q.val: return False
        if not self.traversal(p.right,q.right, res): return False
        return True
        