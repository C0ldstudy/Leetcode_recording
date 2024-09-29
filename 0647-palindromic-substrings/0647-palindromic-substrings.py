class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0
        n = len(s)
        for i in range(n):
            dp[i][i] = True
            res += 1
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1
        
        for length in range(3, n+1):
            for i in range(n-length+1):
                if dp[i+1][i+length-2] and (s[i] == s[i+length-1]):
                    dp[i][i+length-1] = True
                    res += 1
        return res
            