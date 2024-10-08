# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        # stack = [root]
        ans = []
        
        def dfs(node, level):
            ans.append([node.val, level])
            if node.right: 
                dfs(node.right, level+1)
                # stack.append(node.right)
            if node.left:
                dfs(node.left, level+1)
                # stack.append(node.left)
        dfs(root, 0)
        result = []
        for val, level in ans:
            if len(result) <= level: result.append(val)
        # print(ans)
        return result
            