# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        depth = 1
        return max(self.check(root.left, depth), self.check(root.right, depth))
    
    def check(self, node, depth):
        if node:
            depth += 1
            depth = max(self.check(node.left, depth), self.check(node.right, depth))
        return depth

            
        
        