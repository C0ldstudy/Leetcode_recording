class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2): self.gcdOfStrings(str2, str1)
        
        def check(st, st_d):
            time = len(st)//len(st_d)
            if st == st_d * time: return True
            return False
        
        l = len(str2)
        while l > 0:
            if check(str1, str2[:l]) and check(str2, str2[:l]): 
                return str2[:l]
            else:
                # if l % 2 != 0: return "" 
                l -= 1
            # print(l)
        return ""

        
    