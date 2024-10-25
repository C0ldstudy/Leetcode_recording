class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = Counter(s)
        single = 0
        for c in cnt:
            if cnt[c] % 2 == 1:
                single += 1
                if single == 2:
                    return False
        return True
            
                
                