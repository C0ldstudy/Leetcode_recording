class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 2
        result = self.climbStairs(n-1)+self.climbStairs(n-2)
        return result