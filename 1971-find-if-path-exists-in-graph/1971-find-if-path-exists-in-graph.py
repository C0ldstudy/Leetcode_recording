class UF:
    def __init__(self):
        self.data = {}
    def find(self, x):
        y = self.data.get(x, x)
        if y != x:
            self.data[x] = y = self.find(y)
        return y
    def union(self, x, y):
        self.data[self.find(x)] = self.find(y)
        
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UF()
        for e in edges:
            uf.union(e[0], e[1])
        if uf.find(source) == uf.find(destination): return True
        return False
            
        
        