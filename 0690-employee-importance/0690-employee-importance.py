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
        map_dict = {}
        for e in employees:
            # print(e.id)
            map_dict[e.id] = {}
            map_dict[e.id]['neighbor'] = e.subordinates
            map_dict[e.id]['score'] = e.importance
            # if e[0] in map_dict.keys():
        
        res = 0
        stack = [id]
        while stack:
            curr = stack.pop()
            res += map_dict[curr]['score']
            if map_dict[curr]['neighbor']:
                for e in map_dict[curr]['neighbor']:
                    stack.append(e)
        return res
                
            
        