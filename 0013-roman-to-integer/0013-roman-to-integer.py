class Solution:
    def romanToInt(self, s: str) -> int:
        D = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        score = 0
        for i in range(len(s)):
            if i == (len(s)-1):
                score += D[s[i]]
            elif D[s[i]] >= D[s[i+1]]:
                score += D[s[i]]
            else:
                score -= D[s[i]]
            
        return score
                    
        