class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        # if s == '00': return 1
        for i in range(len(s)-1):
            score = self.cal(s, i)
            if score > max_score:
                max_score = score
                # print(i, score)
        return max_score
    def cal(self, s, i):
        score = 0
        for l in range(i+1):
            if s[l] == '0':
                score += 1
        # print(score)
        for l in range(i+1, len(s)):
            if s[l] == '1':
                score += 1
        # print(score)

        return score
                
            
        