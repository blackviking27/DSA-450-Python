# Edit Distance

class Solution:
    def operations(self, s1, s2, n, m):
        if n == 0:
            return m
        if m == 0:
            return n
        
        if self.dp[n][m] != -1:
            return self.dp[n][m]
        
        if s1[n -1] == s2[m -1]:
            if self.dp[n][m] == -1:
                self.dp[n][m] = self.operations(s1, s2, n-1, m-1)
                return self.dp[n][m]
            else:
                return self.dp[n][m]
        else:
            # removing the character from string 1
            if self.dp[n -1][m] != -1:
                m1 = self.dp[n -1][m]
            else:
                m1 = self.operations(s1, s2 ,n-1, m)
                
            # inserting a character
            if self.dp[n][m-1] != -1:
                m2 = self.dp[n][m-1]
            else:
                m2 = self.operations(s1, s2, n, m - 1)

            # replacing the character
            if self.dp[n-1][m-1] != -1:
                m3 = self.dp[n-1][m-1]
            else:
                m3 = self.operations(s1, s2, n-1, m-1)
        self.dp[n][m] = 1 + min(m1, m2, m3)
        return self.dp[n][m]



    def edit_distance(self, s, t):
        n = len(s)
        m = len(t)
        # stores the number of operations required to match string `s` of length n and `t` of len m
        self.dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]
        return self.operations(s, t, n, m)