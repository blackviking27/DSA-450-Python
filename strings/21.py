# Count Palindromic Subsequences 

class Solution:
    def func(self, i, j):
        if i > j: return 0

        # if the answer is already calculated for i, j
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        
        # if not calculated already
        if i == j: # single character is also a palindrome
            self.dp[i][j] = 1
            return 1

        elif self.string[i] == self.string[j]: # if ending characters are equal
            self.dp[i][j] = self.func(i+ 1, j) + self.func(i, j-1) + 1
            return self.dp[i][j]
        else: # if both the characters are not equal
            self.dp[i][j] = self.func(i+1, j) + self.func(i, j-1) - self.func(i+1, j-1)
            return self.dp[i][j]

    def countPs(self, string):
        n = len(string)
        self.dp =[[-1 for x in range(n)] for y in range(n)]
        self.string = string
        return self.func(0, n -1)
    
    # withput recursion method
    def countPs_2(self, string):
        n = len(string)

        # stores the value number of palindromes for i and j index
        cps = [[0 for i in range(n + 2)] for y in range(n + 2)]
 
        for i in range(n):
            cps[i][i] =1
        
        for l in range(2, n + 1):
            for i in range(n):
                k = l + i - 1 # k is the last index of the considered string of length l
                if k < n:
                    if string[i] == string[k]:
                        cps[i][k] = cps[i + 1][k] + cps[i][k -1] + 1
                    else:
                        cps[i][k] = cps[i + 1][k] + cps[i][k -1] - cps[i + 1][k - 1]
        return cps[0][n-1] % (10**9 + 7)

ans = Solution()
print(ans.countPs('abcd'))