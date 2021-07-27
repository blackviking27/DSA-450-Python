# 	Maximum sum of pairs with specific difference

class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K):
        # sorting the array in order to get the adjacent elements
        # to have min diff between them
        arr.sort() 

        # dp stores the max sum of pairs till that index
        dp = [0]*N

        for i in range(1,N):
            # storing the max sum till i-1 index element
            # so now the dp[i] has answer for when ith element is not paired with i-1 element
            dp[i] = dp[i-1]

            # if diff between i th and i-1 th element is less then K 
            # then we try to pair and get the max sum
            if arr[i] - arr[i-1] < K:
                if i >= 2: #since for i=1 there would be no dp[i-2]
                    dp[i] = max(dp[i], dp[i-2] + arr[i] + arr[i-1])
                else:
                    dp[i] = max(dp[i], arr[i] + arr[i-1])
        return dp[N-1]