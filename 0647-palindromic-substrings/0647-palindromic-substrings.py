class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        
        for i in range(n):
            dp[i][i] = True
            res += 1
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1
        
        for row in range(3, n+1):
            for col in range(n-row+1):
                if s[col] == s[col+row-1] and dp[col+1][col+row-2]:
                    dp[col][col+row-1] = True
                    res += 1
        return res
                
        