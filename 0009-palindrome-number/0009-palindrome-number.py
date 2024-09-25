class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reverse_x = x[::-1]
        if x == reverse_x:
            return True
        else:
            return False
        