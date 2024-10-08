# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def bfs(node):
            if not node: return None
            if (not node.left) and (not node.right):
                ans[-1].append(node.val)
                return None
            node.left = bfs(node.left)
            node.right = bfs(node.right)
            return node
        
        while root:
            ans.append([])
            root = bfs(root)
            print(ans)
        return ans
                
        