# Longest Common Subsequence 

class Solution:
    def solve(self, x, y, s1, s2):
        if x == -1 or y == -1: return 0

        if self.dp[x][y] != -1: return self.dp[x][y]

        if s1[x] == s2[y]:
            self.dp = 1 + self.solve(x -1, y -1, s1, s2)
            return self.dp[x][y]
        
        a = self.solve(x - 1, y, s1, s2)
        b = self.solve(x, y - 1, s1, s2)
        self.dp[x][y] = max(a, b)
        return self.dp[x][y]
    # recursive solution
    def longest_common_subs(self, x, y, s1, s2):
        self.dp = [[-1 for i in range(y)] for j in range(x)]
        return self.solve(x-1, y -1, s1, s2)

    # iterative solution
    def lcs(self, x, y, s1, s2):
        dp =[[-1 for i in range(y + 1)] for j in range(x + 1)]

        for i in range(x + 1):
            for j in range(y + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i -1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][ j -1])
        return dp[x][y]