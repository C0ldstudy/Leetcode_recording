# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        numbers = set()
        nodes = [root]
        while nodes:
            cur = nodes.pop()
            if k-cur.val in numbers:
                return True
            numbers.add(cur.val)
            if cur.left:
                nodes.append(cur.left)
            if cur.right:
                nodes.append(cur.right)
        return False