# Weighted Job Scheduling in O(n Log n) time
# Question link leet code -> https://leetcode.com/problems/maximum-profit-in-job-scheduling/

# Declaring a Job object which stores the start, finish and profit of a job
def max_profit(start, finish, profit):
    n = len(start)
    # conatins each job
    jobs = []
    for i in range(n):
        jobs.append([start[i], finish[i], profit[i]])
    
    # sort the jobs according to their finish time
    jobs.sort(key = lambda x: x[1])

    # storing the max profit till that point in time 
    dp = [0]*n
    dp[0] = jobs[0][2] # taking the first profit of the first job

    # Traversing theough each element then calculating the total profit till that point
    # and storing in that position
    for i in range(1, n):
        inc = jobs[i][2] # including the current profit
        last = -1 # stores the position of the element which has no overlap with the current element
        low = 0
        high = i - 1
        while low <= high:
            mid = (low + high) // 2
            if jobs[mid][2] <= jobs[i][0]:
                last = mid
                low = mid + 1
            else:
                high = mid - 1
        if last != -1:
            inc += dp[last]
        exc = dp[i-1]
        dp[n] = max(inc, exc)
    return dp[n-1]

