class Solution:
    def romanToInt(self, s: str) -> int:
        value_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        score = 0
        for i in range(len(s)-1):
            if value_dict[s[i]] >= value_dict[s[i+1]]:
                score += value_dict[s[i]]
            else:
                score -= value_dict[s[i]]
        score += value_dict[s[-1]]
        return score
        