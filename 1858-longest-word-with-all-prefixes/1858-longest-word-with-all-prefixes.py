class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        valid = set()
        res = ""
        for current in words:
            if len(current) == 1 or current[:-1] in valid:
                valid.add(current)
                if len(current) > len(res):
                    res = current
        return res
        
            