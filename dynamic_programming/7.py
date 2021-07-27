# Partition Equal Subset Sum 

class Solution:

    def solve(self, n, arr, s):
        if n == -1: # if there are no elements left 
            if s == 0:# if sum is zero then answer is possible
                return 1
            return 0 #  when sum is not zero which means answer is not possible
        if s < 0: # if sum is negative then answer is not possible
            return 0
        
        if s == 0: #  if sum is zero
            return 1

        if self.dp[n][s] != -1: return self.dp[n][s] # if already calculated for current n, s value

        # when not calculated for current n, s value
        self.dp[n][s] = self.solve(n - 1, arr, s) or self.solve(n -1, arr, s - arr[n]) 
        return self.dp[n][s]

    def partition(self, n, arr):
        s = 0
        for i in range(n):
            s += arr[i]
        # if sum is odd return false
        if s % 2 != 0:
            return 0

        # create dp to store the value
        self.dp = [[-1 for i in range((s//2) + 1)] for j in range(n + 1)]
        return self.solve(n-1, arr, s//2)
    
    # iterative approach
    def equalPartition(self, n, arr):
        s = 0
        for i in range(n):
            s += arr[i]
        if s % 2 != 0:
            return 0
        dp = [[1 for i in range(n+1)] for j in range((s//2) + 1)]

        for i in range(1, (s//2) + 1):
            dp[i][0] = 0

        
        for i in range(1, (s//2) + 1):
            for j in range(1, n + 1):
                # if the current element is greater than the sum
                dp[i][j] = dp[i][j - 1]

                # if the current element is less than the sum
                if i >= arr[j - 1]:
                    # `excluding the last element` or `including the last element`
                    dp[i][j] = dp[i][j - 1] or dp[i - arr[j - 1]][j - 1]
        return dp[s//2][n]

