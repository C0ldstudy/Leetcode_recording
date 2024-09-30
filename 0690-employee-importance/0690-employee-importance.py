"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj = {}
        for e in employees:
            adj[e.id] = {}
            adj[e.id]['imp'] = e.importance
            adj[e.id]['sub'] = e.subordinates
        
        res = 0
        # print(adj[id])
        stack = [adj[id]]
        while stack:
            node = stack.pop()
            # print(node)
            res += node['imp']
            for new in node['sub']:
                stack.append(adj[new])
        return res