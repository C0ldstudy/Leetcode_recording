class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        j = primeOne * primeTwo

#         dp = [False] * j
#         dp[primeOne] = True
#         dp[primeTwo] = True

#         for i in range(j):
#             dp[i] = dp[i] or dp[i - primeOne] or dp[i - primeTwo]
        
#         for k in range(j - 1, -1, -1):
#             if not dp[k]:
#                 return k
        
        return j - primeOne - primeTwo