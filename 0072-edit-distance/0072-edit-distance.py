class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[None for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        def recur(word1, word2, wordindex1, wordindex2):
            if wordindex1 == 0: return wordindex2
            if wordindex2 == 0: return wordindex1
            if memo[wordindex1][wordindex2] is not None:
                return memo[wordindex1][wordindex2]
            minDistance = 0
            if word1[wordindex1-1] == word2[wordindex2-1]:
                minDistance = recur(word1, word2, wordindex1-1,wordindex2-1)
            else:
                insert = recur(word1, word2, wordindex1, wordindex2-1)
                delete = recur(word1, word2, wordindex1-1, wordindex2)
                replace = recur(word1, word2, wordindex1-1,wordindex2-1)
                minDistance = min(insert, delete, replace)+1
            memo[wordindex1][wordindex2] = minDistance
            return minDistance
        return recur(word1, word2, len(word1), len(word2))