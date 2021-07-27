# Longest Repeating Subsequence

class Solution:
    def LongestRepeatingSubsequence(self, string):
        n = len(string)
        dp = [[[-1 for i in range(n + 1)]] for j in range(n + 1)]
        for i in range(n + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                
                elif string[i - 1] == string[j - 1] and i != j:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j -1])
        return dp[n][n]