class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        s = sentence.split(' ')
        for idx in range(len(s)-1):
            if s[idx][-1] != s[idx+1][0]:
                return False
        return True