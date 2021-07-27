# BBT counter 

class Solution:
    def count(h):
        # dp[i] stores the max num of balanced binary tree possible with height i
        dp = [0]*(h+1)

        dp[0] = 1
        dp[1] = 1

        mod = 10**9 + 7

        for i in range(2, h + 1):
            dp[i] = (dp[i-1] * ((2*dp[i-2])%mod + dp[i-1]%mod))%mod
        
        return dp[h]
