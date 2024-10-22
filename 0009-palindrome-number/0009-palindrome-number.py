class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x = list(str(x))
        length = len(x)//2
        for i in range(length):
            if x[i] != x[-i-1]:
                return False
        return True