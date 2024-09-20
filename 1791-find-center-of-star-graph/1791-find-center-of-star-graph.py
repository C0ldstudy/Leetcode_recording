class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        node_number = max(max(e) for e in edges)
        count = [0 for i in range(node_number)]
        for i, e in enumerate(edges):
            count[e[0]-1] += 1
            count[e[1]-1] += 1
            if count[e[0]-1] == (node_number-1):
                return e[0]
            elif count[e[1]-1] == (node_number-1):
                return e[1]
            
        
            