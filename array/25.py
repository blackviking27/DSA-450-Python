# Maximum profit by buying and selling a share atmost twice
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.

class Solution:
    def max_dp(self, prices):
        n = len(prices)
        dp = [0]*n # stores the profit till that point
        ma = prices[n-1] # taking the last as the max sell
        mi = prices[0] # taking the initial as minimum buy
        
        # right iteration
        for i in range(n-2 , -1, -1):
            if prices[i] > ma:
                ma = prices[i]
            dp[i] = max(dp[i + 1], ma - prices[i])
        
        # left iteration
        for i in range(1, n):
            if prices[i] < mi:
                mi = prices[i]
            dp[i] = max(dp[i -1], dp[i] + (prices[i] - mi))
        
        return dp[n-1]

    # without dynamic programming
    # for explanantion: https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-stock-at-most-twice-set-2/?ref=rp
    def max_simple(self, prices, n):
        buy1 = buy2 = float('inf')
        profit1 = profit2 = 0
        for i in range(n):
            # buying the stock with our money
            # at min price, if we bought at low price before we don't need
            # to buy again
            buy1 = min(buy1, prices[i])

            # sell the stock to make a profit
            # for the first stock
            profit1 = max(profit1, prices[i] - buy1)

            # integrating the profit we made to reduce 
            # the buying price of the stock
            buy2 = min(buy2, prices[i] - profit1)

            # making a profit on second stock
            profit2 = max(profit2, prices[i] - buy2)

        return profit2