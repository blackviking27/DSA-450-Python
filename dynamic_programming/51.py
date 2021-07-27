# Word Wrap
class Solution:
    def solveWordWrap(self,arr, k):
        n = len(arr)
        # stores the minimum cost
        dp = [0]*n

        # if only 1 word is present then cost of one word is zero
        dp[n - 1] = 0
        # ans[n - 1] = n - 1 # stores the last index for the last word

        for i in range(n -2, -1, -1):
            curr_len = -1
            dp[i] = float('inf') # max cost if we are unable to fit the words in one line
            for j in range(i, n):
                # updating the current length, we add the number of characters in arr[i]
                # and 1 which shows the space between each word
                curr_len += (arr[j] + 1)

                if curr_len > k: # we are unable to fit the characters in a single line
                    break 
                
                # for last line we need not calculate the cost of line
                if j == n - 1:
                    cost = 0
                else:
                    cost = (k - curr_len)**2 + dp[j + 1]
                
                dp[i] = min(cost, dp[i])
        return dp[0]
            