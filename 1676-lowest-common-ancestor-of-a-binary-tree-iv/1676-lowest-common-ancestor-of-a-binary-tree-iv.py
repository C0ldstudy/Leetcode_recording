# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        if (root == None) or  (root in nodes): 
            return root
        l = self.lowestCommonAncestor(root.left, nodes)
        r = self.lowestCommonAncestor(root.right, nodes)
        if l and r:
            return root
        else:
            return l or r