# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lca(self, root, p, q):
        if root in (None, p, q): return root
        l = self.lca(root.left, p, q)
        r = self.lca(root.right, p, q)
        if l and r:
            return root
        else:
            return l or r
    
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a = []
        def dfs(node, h):
            if not node:
                return
            if len(a) == h:
                a.append([])
            a[h].append(node)
            dfs(node.left, h+1)
            dfs(node.right, h+1)
        dfs(root, 0)
        print(a)
        p, q = a[-1][0], a[-1][-1]
        return self.lca(root, p, q)
    
