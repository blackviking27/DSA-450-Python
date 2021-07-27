# Binomial CoefficientProblem
# meathematical formula => nCr = n-1Cr-1 + n-1Cr

class Solution:
    def nCr(self, n, k):
        # for each value of n the dp stores the nCk value in it
        # ex: for n = 1 the dp would store 1Ck value where k would be index in the dp
        # for n = 2 the dp would store 2Ck value
        dp = [0 for i in range(k + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            j = min(i, k)
            while j > 0:
                dp[j] += dp[j - 1]
                j -= 1
        return dp[k] % (10**9 + 7)
    
    # withour extra space and O(n) time
    def binomial_coefficient(self, n, k):
        if k > n - k:
            k = n - k # since C(n, k) = C(n, n -k)
        
        res = 1
        # since C(n, k) = [ n*(n-1)*(n-2).....*(n-(k -1)) ] / [1*2*......*(k-1)*k]
        for i in range(k):
            res = res * (n - i)
            res = res / (i + 1)
        return res