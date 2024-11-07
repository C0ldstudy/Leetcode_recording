class Solution:
    def isPalindrome(self, s: str) -> bool:
        ps = ''
        for i in s.lower():
            if i.isalnum():
                ps += i
        # print(ps)
        length = len(ps)//2
        for i in range(length):
            if ps[i] != ps[-i-1]:
                return False
        return True