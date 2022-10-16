class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        elif len(jobDifficulty) == d:
            return sum(jobDifficulty)
        dp = [[float('inf')]*len(jobDifficulty) for i in range(d)] # d *jobs
        dp[0][0] = jobDifficulty[0]
        for i in range(1, len(jobDifficulty)):
            if i < d:
                dp[i][i] = sum(jobDifficulty[:i+1])
            dp[0][i] = max(dp[0][i-1], jobDifficulty[i])

        for j in range(1, d):
            for i in range(j+1, len(jobDifficulty)):
                for k in range(i):
                    dp[j][i] = min(dp[j][i], dp[j-1][k] + max(jobDifficulty[k+1:i+1]))
        return dp[d-1][len(jobDifficulty)-1]
                
        

        
            
        
        