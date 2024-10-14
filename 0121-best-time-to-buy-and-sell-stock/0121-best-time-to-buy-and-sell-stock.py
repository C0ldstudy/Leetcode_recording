class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_idx = 0
        for i in range(1, len(prices)):
            if prices[i]< prices[buy_idx]:
                buy_idx = i
            elif prices[i] > prices[buy_idx]:
                if profit < (prices[i] - prices[buy_idx]):
                    profit = prices[i] - prices[buy_idx]
        return profit
                

        