# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        stack = deque([(root, 0)])
        
        def bfs(stack):
            # print(stack)
            res = {}
            while stack:
                node, line = stack.popleft()
                if line not in res.keys():
                    res[line] = [node.val]
                else:
                    res[line].append(node.val)
                if node.left: stack.append((node.left,line-1))
                if node.right: stack.append((node.right, line+1))
            return res
        res = bfs(stack)
        return [res[i] for i in sorted(res.keys())]
            