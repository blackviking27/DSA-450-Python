# Longest subsequence such that difference between adjacent is one

class Solution:
    def longestSubsequence(self, n, arr):
        dp = [1 for i in range(n)]
        
        # following LIS approach but we store the length of max subsequence with diff 1 between adjacent elements
        for i in range(n):
            for j in range(i):
                if arr[i] == arr[j] + 1 or arr[i] == arr[j] - 1:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        res = 1
        for i in range(n):
            if dp[i] > res:
                res = dp[i]
        return res