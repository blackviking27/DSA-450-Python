# Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices) -> int:
        sell = 0
        buy = prices[0]
        for pr in prices:
            if pr <= buy:
                buy = pr
            else:
                if pr - buy > sell:
                    sell = pr - buy
        return sell
        