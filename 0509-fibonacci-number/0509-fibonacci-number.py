class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        n1, n2 = 0, 1
        for ni in range(n-1):
            n_new = n1 + n2
            n1 = n2
            n2 = n_new
        return n_new
        
        