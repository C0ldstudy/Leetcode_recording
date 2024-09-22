class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = {}
        for i in s:
            if i in c.keys():
                c[i] += 1
            else:
                c[i] = 1
        number = 0
        for i in c.keys():
            if c[i] % 2 == 0:
                number += c[i]
            else:
                number += c[i] - 1
        if number != len(s): return number+1
        return number
                
            
        