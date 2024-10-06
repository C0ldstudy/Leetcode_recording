class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) < len(sentence2): return self.areSentencesSimilar(sentence2, sentence1)
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        
        start = 0
        end1 = len(s1)-1
        end2 = len(s2)-1
        while start < len(s2) and s2[start]==s1[start]:
            start += 1
        while end2 >= 0 and s2[end2] == s1[end1]:
            end1 -= 1
            end2 -= 1
        print(start, end2)
        if end2 < start: return True
        return False
            
        