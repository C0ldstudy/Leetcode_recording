# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        gap_node = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if abs(target-node.val) < abs(target - gap_node):
                gap_node = node.val
            elif abs(target-node.val) == abs(target - gap_node):
                gap_node = min(node.val, gap_node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return gap_node
            