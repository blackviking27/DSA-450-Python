# Space Optimized Solution of LCS

class Solution:
    def lcs(self, x, y, s1, s2):
        dp = [[-1 for i in range(y + 1)] for j in range(2)]

        bi = bool
        for i in range(x + 1):
            bi = i&1 # taking one of the two rows
            for j in range(y + 1):
                if i == 0 or j == 0:
                    dp[bi][j] = 0
                elif s1[i - 1] == s2[j - 1]:
                    dp[bi][j] = dp[1 - bi][j - 1] + 1
                else:
                    dp[bi][j] = max(dp[1 -bi][j], dp[bi][j - 1])
        return dp[bi][y]


