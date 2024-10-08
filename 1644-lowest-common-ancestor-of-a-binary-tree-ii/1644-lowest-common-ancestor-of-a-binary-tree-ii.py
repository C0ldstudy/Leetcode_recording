# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(stack, p):
            while stack:
                node = stack.pop()
                if node == p: return True
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            return False
        
            
        def LCA(root, p, q):    
            if root in (None, p, q): 
                return root
            l = LCA(root.left, p ,q)
            r = LCA(root.right, p, q)
            if l and r:
                return root
            else:
                return l or r
        
        
        if dfs([root], p) and dfs([root], q):
            return LCA(root, p, q)
        else:
            return None
