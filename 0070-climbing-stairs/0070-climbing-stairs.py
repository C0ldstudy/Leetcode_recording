class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        elif n == 2: return 2
        elif n == 3: return 3
        dp = [0] * (n+1)
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
            