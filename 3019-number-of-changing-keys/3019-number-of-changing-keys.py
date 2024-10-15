class Solution:
    def countKeyChanges(self, s: str) -> int:
        if len(s) <= 1: return 0
        s = s.lower()
        count = 0
        for idx in range(1, len(s)):
            if s[idx] != s[idx-1]:
                count += 1
        return count
        
        