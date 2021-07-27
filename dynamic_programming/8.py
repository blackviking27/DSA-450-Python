# Friends Pairing Problem

class Solution:

    def solve(self, n):
        if n <= 2:
            return n
        
        if self.dp[n] != -1: return self.dp[n]

        self.dp[n] = self.solve(n-1)%(self.mod) + (((n - 1)%self.mod)*self.solve(n - 2)%self.mod)%self.mod
        return self.dp[n]


    def pait_dp(self, n):
        self.dp = [-1]*(n + 1)
        self.mod = 10**9 + 2

    def pair(self, n):
        
        # Number of ways the people can form a group is
        # sum of when they decide to be single + whe they decide to pair up
        # when a person stays single then the rest people decide if they want to pair up or stay single
        # when they decide to pair up then there are n-1 ways  possible and for each pairing the rest of 
        # n-2 people make the decision to either pair up or not
        # f(n) = f(n-1) + (n-1)*f(n-2)
        a, b, c = 1, 2, 0
        if n <=2 :
            return n
        
        mod = 10**9 + 7
        for i in range(3, n+1):
            c = (b%mod + (i -1)*a%mod)%mod
            a = b%mod
            b = c%mod
        return c