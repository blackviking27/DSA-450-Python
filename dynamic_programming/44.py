# Weighted Job schedule
# Practice question link https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = []
        n = len(startTime)
        for i in zip(startTime, endTime, profit):
            jobs.append(i)
        
        jobs.sort(key=lambda x: x[1])

        dp = [0]*n
        dp[0] = jobs[0][2] # storing the profit of first job

        for i in range(1, n):
            last = -1 # points to the last index of the element
            low = 0
            high = i - 1

            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    last = low
                    low = mid + 1
                else:
                    high = mid - 1
            
            include = jobs[i][2] # stores the profit when we include the current job is included
            if last != -1: include += dp[last]
            exclude = dp[i - 1] # stores the profit when we exclude the current job

            dp[i] = max(include, exclude)
        
        return dp[n-1]