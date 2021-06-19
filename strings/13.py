# Edit Distance
#  video explanation on YouTube => https://www.youtube.com/watch?v=AuYujVj646Q (I found this one to be fairly good for explanation)

class Solution:
    def operation(self, s, t, n, m, dp):
        # if the first string is over then add n characters to the first string
        if n == 0: return m

        # if the second string is over then remove m characters from the first string
        if m == 0: return n
        
        # checking if answer is already calculated for current n and m
        if dp[n][m] != -1: 
            return dp[n][m]

        # if the last character of the strings are same
        # then just move to next character, since it is zero indexing we are taking -1 for position
        if s[n - 1] == t[m -1]:
            if dp[n - 1][m - 1] == -1:
                dp[n][m] = self.operation(s, t, n - 1, m - 1, dp)
                return dp[n][m]
            else:
                # returning the same number of operations for n, m as n - 1, m -1
                dp[n][m] = dp[n -1][m - 1]
                return dp[n][m]
        else:
            # removing the current character in string 1
            if dp[n - 1][m] != -1:
                m1 = dp[n -1][m]
            else:
                m1 = self.operation(s, t, n -1, m, dp)
            
            # inserting a character in string 1
            if dp[n][m - 1] != -1:
                m2 = dp[n][m - 1]
            else:
                m2 = self.operation(s, t, n, m - 1, dp)
            
            # replacing the current character in string 1
            if dp[n - 1][m - 1] != -1:
                m3 = dp[n -1][m -1]
            else:
                m3 = self.operation(s, t, n - 1, m -1, dp)
        

        dp[n][m] = 1 + min(m1, min(m2, m3))
        return dp[n][m]

    def editDistance(self, s, t):
        n = len(s) # length of string 1
        m = len(t) # length of string 2

        # dp = [[0 for col in columns] for r in rows]
        dp = [[-1 for x in range(n + 1)] for y in range(m + 1)]
        return self.operation(s, t, n, m, dp)