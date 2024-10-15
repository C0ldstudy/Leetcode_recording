class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for idx in range(1, len(s)):
            score += abs(ord(s[idx])-ord(s[idx-1]))
            # print(score)
        return score