class Solution:
    def shortestPalindrome(self, s: str) -> str:
        mid = int(len(s)/2)
        for i in range(mid, 0, -1):
            result = self.check(i, s)
            if result == "Type 1":
                return self.generate(i, s, "1")
            elif result == "Type 2":
                return self.generate(i, s, "2")
        return self.generate(0,s, "1")
    
    def check(self, i, s):
        length = len(s[:i])
        # print(s[i:i+length], s[:i])
        if s[i+1:i+1+length][::-1] == s[:i]:
            return "Type 1"
        elif s[i:i+length][::-1] == s[:i]:
            return "Type 2"     
        else:
            return False
    def generate(self, i, s, t):
        if t == "1":
            result = s[i+1:][::-1]+s[i:]
        elif t == "2":
            result = s[i:][::-1]+s[i:]
        return result
    
        