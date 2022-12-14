### 309. Best Time to Buy and Sell Stock with Cooldown
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

### Key idea
- DP: `buy[i] = max(sell[i-2]-price, buy[i-1])`



### Solution
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 1: return 0
        prev_sell, sell, buy = 0, 0, -prices[0] # buy initialized to buying a stock at i=0
        for i in range(1, len(prices)):
            prev_sell, sell, buy = sell, max(buy+prices[i], sell), max(prev_sell-prices[i], buy)
        return max(sell, buy)
```
