class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(' ')
        s2 = s2.split(' ')
        cnt = Counter(s1+s2)
        res = []
        for c in cnt:
            if cnt[c] == 1:
                res.append(c)
        return res
                