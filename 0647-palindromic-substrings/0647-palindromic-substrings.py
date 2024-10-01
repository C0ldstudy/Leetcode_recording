class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] *len(s) for _ in range(len(s))]
        res = 0
        for i in range(len(s)):
            dp[i][i] = True
            res += 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1
        n = len(s)    
        print(res)
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length-1
                if (dp[i+1][j-1] == True) and (s[i] == s[j]):
                    dp[i][i+length-1] = True
                    res += 1
        return res