# Optimal Strategy For A Game

def solve(i, j, arr, dp):
    if i > j: return 0
    if dp[i][j] != -1: return dp[i][j]

    x = arr[i] + min(solve(i + 2, j, arr, dp), solve(i + 1, j - 1, arr, dp))
    y = arr[j] + min(solve(i, j - 2, arr, dp), solve(i + 1, j - 1, arr, dp))
    dp[i][j] = max(x, y)
    return dp[i][j]

def optimalStratergy(arr, n):
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    return solve(0, n-1, arr, dp)