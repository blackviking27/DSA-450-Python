# Longest Increasing Subsequence

from bisect import bisect
class Solution:
    def longestSubsequence(self, a, n):
        dp = [float('inf')]*(n + 1)
        dp[0] = float('-inf')

        for i in range(n):
            idx = bisect(dp, a[i]) # finding the upper bound for the current element in dp
            if a[i] > dp[idx - 1] and a[i] < dp[idx]: # if the element lies between the value of dp[idx-1] and dp[idx]
                dp[idx] = a[i]
        
        for i in range(n, -1, -1):
            if dp[i] != float('inf'):
                return i
        return 0 # if we did not find the increasing common subsequence 
