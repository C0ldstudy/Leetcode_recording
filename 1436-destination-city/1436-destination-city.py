class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        arrivals, dests = [], []
        for i,j in paths:
            arrivals.append(j)
            dests.append(i)
        for a in arrivals:
            if not (a in dests):
                return a
        return 
        