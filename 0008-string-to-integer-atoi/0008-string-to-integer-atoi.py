class Solution:
    def myAtoi(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] != ' ':
                s = s[i:]
                break
        print(s)
        if len(s) == 0: return 0
        flag = 1
        if s[0] == '-': 
            flag *= -1
            s = s[1:]
        elif s[0] == '+':
            flag *= 1
            s = s[1:]
        elif not s[0].isdigit(): 
            return 0
        print(s)
        if len(s) == 0: return 0

        if not s[0].isdigit(): return 0
        for i in range(len(s)):
            if not s[i].isdigit():
                s = s[:i]
                break
        print(s)
        number = int(s)
        print(s, number)
        
        if (flag*number) > 2**31-1: return (2**31-1)
        if (flag*number) < -2**31: return -2**31
        print((flag*number))
        return (flag*number)
            
            