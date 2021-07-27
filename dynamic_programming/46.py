# Disarrangement of balls 

class Solution:
    # recursive solution
    def dearrange_recur(self, n):
        if n == 1: return 0
        if n == 2: return 1

        return (n - 1) * (self.dearrange_recur(n - 1) + self.dearrange_recur(n - 2))

    # iterative solution
    def disarrange(self, n):
        dp = [0]*(n + 1)
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = (i - 1)*(dp[i-1] + dp[i - 2])
        
        return dp[n]

    # efficient solution
    def disarrange_efficient(self, n):
        
        if n == 1 or n == 2: return n - 1

        a = 0
        b = 1
        mod = 10**9 + 7

        for i in range(3, n + 1):
            curr = ((i - 1)*(a + b))%mod
            a = b
            b = curr
        return b % (10**9 + 7)