# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        map_dic = {}
        queue = deque([(root, 0)])
        
        while queue:
            node, line = queue.popleft()
            if not line in map_dic:
                map_dic[line] = []
            map_dic[line].append(node.val)
            if node.left: queue.append((node.left, line-1))
            if node.right: queue.append((node.right, line+1))
        
        # print(map_dic)
        return [map_dic[i] for i in sorted(map_dic.keys())]
        # res = 
                