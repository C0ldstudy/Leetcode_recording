"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':        
        
        def root_find(node):
            if node.parent == None:
                return node
            else:
                node = root_find(node.parent)
            return node
        root = root_find(p)
        
        def LCA(root, p, q):
            if root in (None,p, q): return root
            l = LCA(root.left, p, q)
            r = LCA(root.right, p ,q)
            if l and r:
                return root
            else:
                return l or r
        return LCA(root, p ,q)
            