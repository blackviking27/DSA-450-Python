# Partition Equal Subset Sum

class Solution:
    def solve(self, n, arr, s):
        if n == -1: # if we have reached the last element
            if s == 0: # if we found the sum
                return True
            return False
        if s < 0:
            return False
        
        if s == 0:
            return True

        if self.dp[n][s] != -1: return self.dp[n][s]

        self.dp[n][s] = self.solve(n-1, arr, s) or self.solve(n-1, arr, s-arr[n])
        return self.dp[n][s]


    def equalPartition(self, n, arr):
        s = 0 # sum of the nums
        for el in arr:
            s += el
        if s % 2 != 0:
            return 0
        
        self.dp = [[-1 for i in range(s//2 + 1)] for i in range(n + 1)]
        return self.solve(n-1, arr, s//2)
