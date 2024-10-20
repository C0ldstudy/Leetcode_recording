import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = 'ag ct oso gcota'
        s = re.sub('[^a-z0-9]', '', s.lower())
        # print(s)
        length = len(s)//2
        for i in range(length):
            if s[i] != s[-i-1]:
                return False
        return True