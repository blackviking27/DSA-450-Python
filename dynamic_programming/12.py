# Maximize The Cut Segments 

class Solution:
    def maximizeTheCuts(self,n,x,y,z):
        dp = [-1]* (n + 1)
        dp[0] = 0 # since 0 cuts are required for rod of length 0
        
        for i in range(n + 1):
            if dp[i] == -1:
                continue
            
            if i + x <= n:
                dp[i+x] = max(dp[i + x], dp[i] + 1)
            if i + y <= n:
                dp[i+y] = max(dp[i + y], dp[i] + 1)
            if i + z <= n:
                dp[i+z] = max(dp[i + z], dp[i] + 1)
                
        if dp[n] < 0:
            dp[n] = 0
        return dp[n]
