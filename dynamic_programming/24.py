# Maximum size square sub-matrix with all 1s

class Solution:
    def maxSide(self, n, m, mat):

        # dp[i][j] stores the value for max_side for the mat[i-1][j-1]
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        max_side = 0 # stores the length of max_side

        # if mat[i][j] is 1 then in the dp we look for min in up, left and diagonally left up
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if mat[i-1][j-1] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    max_side = max(max_side, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_side