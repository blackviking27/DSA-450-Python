# Maximum subsequence sum such that no three are consecutive

# iterative approach
def consecutive_sum_3(arr):
    n = len(arr)

    dp = [0 for i in range(n)]

    if n >= 1: # for first element max sum is element itslef 
        dp[0] = arr[0]
    
    if n >= 2: # for second element max sum if sum first and second element
        dp[1] = arr[0] + arr[1]
    
    if n > 2: # for third it is max of sum of (1st and 3rd) or (2nd and 3rd) or (1st and 2nd) 
        dp[2] = max(dp[1], max(arr[1] + arr[2], arr[0] + arr[2]))
    
    for i in range(3,n):
        # we have three caese
        # 1. ignore ith element => dp[i-1]
        # 2. ignore the i-1th element => dp[i-2] + arr[i]
        # 3. ignore the i-2th element => dp[i-3] + arr[i-1] + arr[i]
        dp[i] = max(dp[i -1], max(dp[i-2] + arr[i], dp[i - 3] + arr[i -1] + arr[i]))
    
    return dp[n-1]

# Driver code
arr = [100, 1000, 100, 1000, 1]
print(consecutive_sum_3(arr))