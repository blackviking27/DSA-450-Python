# Knapsack with Duplicate Items 

class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [0]*(W+1)

        for i in range(W + 1):
            for j in range(N):
                dp[i] = max(dp[i], dp[i-wt[j]] + val[j])
        
        return dp[W]