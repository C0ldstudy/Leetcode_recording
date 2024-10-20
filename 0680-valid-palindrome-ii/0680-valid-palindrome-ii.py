class Solution:
    def validPalindrome(self, s: str) -> bool:
        idx = len(s)//2
        def check(sub):
            sub_idx = len(sub)//2
            for i in range(sub_idx):
                if sub[i] != sub[-i-1]:
                    return False
            return True
            
            
        
        for i in range(idx):
            if s[i] != s[-i-1]:
                s1 = s[:i]+s[i+1:]
                if i != 0:
                    s2 = s[:(-i-1)]+s[-i:]
                else:
                    s2 = s[:(-i-1)]
                # print(s1, s2)
                return any((check(s1), check(s2)))
        return True