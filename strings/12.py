# Word Wrap

class Solution:
    def wordWrap(self, arr, k):
        n = len(arr)
        dp = [0]*n # stores the min line cost for arr[i] as start index
        ans = [0]*n # stores the last index with arr[i] as start

        # if only one word is present
        dp[n - 1] = 0
        ans[n - 1] = n - 1

        # strting from right side ans considering each word as last index
        for i in range(n -2, -1, -1):
            curr_len = -1 # stores the length of all words so far
            dp[i] = float('inf') # considering max length
            for j in range(i, n):
                # adding the current word length and the single space
                curr_len += arr[j] + 1

                # if the current length of line is greater than max length of line, k.
                if curr_len > k:
                    break
                
                # reaching the last word implies that we have reached the last line
                if j == n - 1:
                    cost = 0
                else:
                    cost = k - curr_len + dp[j + 1]
                
                
                