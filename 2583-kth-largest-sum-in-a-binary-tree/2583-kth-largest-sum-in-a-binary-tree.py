# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = {}
        stack = [(root, 0)]
        
        while stack:
            node, level = stack.pop()
            if level in sums:
                sums[level] += node.val
            else:
                sums[level] = node.val
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        result = sorted(list(sums.values()), reverse=True)
        if k > len(result):
            return -1
        else:
        
            return result[k-1]