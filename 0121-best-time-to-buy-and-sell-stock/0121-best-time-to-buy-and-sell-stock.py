class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = math.inf
        amount = 0
        for idx in range(len(prices)):
            if prices[idx] < buy:
                buy = prices[idx]
            elif (prices[idx] - buy) > amount:
                amount = prices[idx] - buy
        return amount
                