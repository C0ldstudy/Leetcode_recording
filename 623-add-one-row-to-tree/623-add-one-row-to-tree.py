# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val)
            new.left = root
            return new
        layer = [root]
        # iteratively collect the nodes in the correct layer
        for i in range(depth-2):
            tmp = []
            for n in layer:
                if n.left != None:
                    tmp.append(n.left)
                if n.right != None:
                    tmp.append(n.right)
            layer = tmp
        # insert the new nodes
        for n in layer:
            tmp_n = n.left
            n.left = TreeNode(val)
            n.left.left = tmp_n
            tmp_n = n.right
            n.right = TreeNode(val)
            n.right.right = tmp_n      
        return root
            
        