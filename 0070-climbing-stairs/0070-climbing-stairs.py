class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        temp = [0] * n
        res = self.check(n-1, n, temp)
        return res
    
    def check(self, i, n , temp):
        if i == 0: return 1
        elif i == 1: return 2
        if temp[i] > 0:
            return temp[i]
        else:
            temp[i] = self.check(i-1, n, temp) + self.check(i-2, n, temp)
        return temp[i]
        