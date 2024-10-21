class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                return False
        if n == 1:
            return True
        else:
            return False