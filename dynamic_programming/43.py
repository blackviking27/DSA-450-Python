# Longest alternating subsequence

class Solution:
    def AlternatingaMaxLength(self, arr):
        m1 = 1
        m2 = 1
        n = len(arr)

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                m1 = m2 + 1
            elif arr[i] < arr[i - 1]:
                m2 = m1 + 1
        
        return max(m1, m2)
    
    # DP approach
    def AlternatingaMaxLength_dp(self, arr):
        n = len(arr)

        # dp[i][0] stores the max length of alternating sequence when ith element is greater than previous
        # dp[i][1] stores the max length of alternating sequence when ith element is less than previous
        dp = [[1 for _ in range(2)] for _ in range(n)]

        res = 1

        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j] and dp[i][0] < dp[j][1] + 1:
                    dp[i][0] = dp[j][1] + 1
                elif arr[i] < arr[j] and dp[i][1] < dp[j][0] + 1:
                    dp[i][1] = dp[j][0] + 1
            res = max(res, max(dp[i][0],dp[i][1]))

        return res