# Count all subsequences having product less than K

def productSubSeqCount(arr, k):
    n = len(arr)
    # dp[i][j] stores the max number of subsequence which has sum less than i with j terms
    dp = [[0 for i in range(n + 1)] for j in range(k + 1)]

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            # taking the previous answer and then we add the number
            # of subsequence possible with current element
            # to the dp
            dp[i][j] = dp[i][j -1]

            if arr[j -1] <= i and arr[j -1] > 0:
                dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1
    return dp[k][n]

# Driver code
A = [1,2,3,4]
k = 10
print(productSubSeqCount(A, k))