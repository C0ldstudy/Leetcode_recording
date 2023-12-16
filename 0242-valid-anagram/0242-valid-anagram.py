class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        # if s == t: return False
        length = len(s)
        t = sorted(list(t))
        s = sorted(list(s))
        for i in range(length):
            if not (s[i] == t[i]): return False
        return True
        