# 	Maximum Sum Increasing Subsequence

class Solution:
    def maxSumIs(self, arr, n):
        dp = [arr[i] for i in range(n)] # storing the value of element at the the index to present the curret max sum

        # looping through each element and then moving from first element 
        # to the element just on the left of the current element. Find the element which is less than
        # current element and take max of dp[i] which shows the current sum for the current element
        # and dp[j] + arr[i] which is sum of max of elements till the jth element plus value of current element
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + arr[i])
        ma = 0
        for i in range(n):
            ma = max(ma, dp[i])
        return ma        