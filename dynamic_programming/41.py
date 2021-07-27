# Count All Palindromic Subsequence in a given String

class Solution:
    def countPs(self,string):
        n = len(string)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        # for string of length 1
        for i in range(n):
            dp[i][i] = 1
        
        for l in range(2, n+1):
            for i in range(n):
                j = i + l - 1
                if j < n:
                    if string[i] == string[j]:
                        dp[i][j] = dp[i][j-1] + dp[i+1][j] + 1
                    else:
                        dp[i][j] = dp[i + 1][j] + dp[i][j -1] - dp[i + 1][j-1]
        return dp[0][n-1] % (10**9 + 7)
                    