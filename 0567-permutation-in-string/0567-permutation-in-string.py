class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = Counter(s1)
        for i in range(len(s2)):
            cnt2 = Counter(s2[i:i+len(s1)])
            # print(cnt2, cnt1)
            if cnt2 == cnt1: return True
        return False
                