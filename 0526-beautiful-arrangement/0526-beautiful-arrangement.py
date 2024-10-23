class Solution:
    def countArrangement(self, n: int) -> int:
        
        visit = [False] * (n+1)
        ans = 0
        def backtrack(index):
            
            if index  == n+1:
                nonlocal ans 
                ans +=1
            
            for i in range(1,n+1):
                if not visit[i]:
                    if i % index == 0 or index % i == 0:
                        visit[i] = True
                        backtrack(index+1)
                        visit[i] = False
                        
        backtrack(1)
        return ans