class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1: return 1
        trust_others = []
        for i in trust:
            trust_others.append(i[0]-1)            
        trust_num = [0 for _ in range(n)]
        
        for i in trust:
            if not (i[1]-1) in trust_others:
                trust_num[i[1]-1] += 1
                if trust_num[i[1]-1] == (n-1):
                    return i[1]
        return -1
        
            
        