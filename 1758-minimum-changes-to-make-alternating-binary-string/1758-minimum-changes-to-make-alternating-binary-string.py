class Solution:
    def minOperations(self, s: str) -> int:
        score1, score2 = 0, 0
        length = len(s)
        type1 = ''
        type2 = ''
        for i in range(length):
            if i % 2 == 0:
                type1 += '0'
                type2 += '1'
            else:
                type1 += '1'
                type2 += '0'
                
        for i in range(length):
            if s[i] != type1[i]:
                score1 += 1
            if s[i] != type2[i]:
                score2 += 1 
        # print(score1, score2)
        return min(score1, score2)