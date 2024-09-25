class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        amount = 0
        buy_amount = float("inf")
        for i in range(0, len(prices)):
            if prices[i] < buy_amount:
                buy_amount = prices[i]
            elif amount < (prices[i]-buy_amount):
                    amount = prices[i]-buy_amount
                    
        return amount
            
            
        