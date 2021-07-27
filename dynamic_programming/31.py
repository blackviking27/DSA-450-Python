# Longest Common Substring 

class Solution:
    def longestCommonSubstr(self, s1, s2, n, m):
        # dp[i][j] stores the longest common substring for i-1, j-1 index in s1, s2
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        res = 0 # stores the answer
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        return res