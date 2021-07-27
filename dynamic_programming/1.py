# 0 - 1 Knapsack Problem

class Solution:
    def knapSack(self,W, wt, val, n):
        # the columns represent the weights possible and
        # rows represent the number of items that are taken
        dp = [[0 for i in range(W + 1)] for i in range(n + 1)]
        
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:# if either no item is present or weight is zero
                    dp[i][w] = 0
                
                elif wt[i - 1] <= w:
                    # if weight if ith item is less than the current weight that we are considering
                    # we take max of (value of latest item i.e i-1 + value of previously calculated 
                    # i - 2 items and the previous calculated value of i -1 items)
                    dp[i][w] = max(val[i - 1] + dp[i -1][w - wt[i - 1]], dp[i -1][w])
                else:
                    dp[i][w] = dp[i -1][w] # if weight greater than take the previous answer
        return dp[n][W]