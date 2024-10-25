class Solution:
    def reverseVowels(self, s: str) -> str:
        target = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        vowel = []
        for i in s:
            if i in target:
                vowel.append(i)
        vowel.reverse()
        cnt = 0
        for idx in range(len(s)):
            if s[idx] in target:
                s[idx] = vowel[cnt]
                cnt += 1
        return ''.join(s)
                
            
            