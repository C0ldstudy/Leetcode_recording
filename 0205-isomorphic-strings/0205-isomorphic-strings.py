class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        for s1, t1 in zip(s,t):
            if (s1 not in map_s) and (t1 not in map_t):
                map_s[s1] = t1
                map_t[t1] = s1
            elif map_s.get(s1) != t1 or map_t.get(t1) != s1:
                return False
        return True