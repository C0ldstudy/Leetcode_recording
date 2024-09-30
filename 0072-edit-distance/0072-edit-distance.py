class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        index1 = len(word1)
        index2 = len(word2)
        
        dp = [ [False] * (len(word2)+1) for _ in range(len(word1)+1) ]        
        
        def check(word1, word2, index1, index2):
            # print(index1, index2)
            if index1 <= 0: 
                return index2
            elif index2 <= 0:
                return index1
            if dp[index1][index2] != False:
                return dp[index1][index2]
            res = 0
            if word1[index1-1] != word2[index2-1]:
                insert = check(word1, word2,index1-1, index2)
                delete = check(word1, word2,index1, index2-1)
                replace = check(word1, word2,index1-1, index2-1)
                res = min(insert, delete, replace) + 1
            else: 
                res = check(word1, word2,index1-1, index2-1)
            dp[index1][index2] = res
            # print(res)
            return res
        res = check(word1, word2, index1, index2)
        # print(dp)
        
        return res
        