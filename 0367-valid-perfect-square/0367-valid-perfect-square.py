class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        cur = 2
        while cur*cur <= num:
            if cur*cur == num:
                return True
            else:
                cur += 1
                
        return False