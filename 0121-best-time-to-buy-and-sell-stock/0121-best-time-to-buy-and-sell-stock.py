class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = math.inf
        max_amount = 0
        for p in prices:
            if p < buy:
                buy = p
            elif (p - buy) > max_amount:
                max_amount = p - buy
        return max_amount