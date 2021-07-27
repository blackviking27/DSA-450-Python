# 	Longest Palindromic Subsequence

# recursive approach
def solve(string, i, j, dp):
    if i == j:
        return 1
    if i > j:
        return 0
    
    if dp[i][j] != 0: return dp[i][j]

    if string[i] == string[j]:
        dp[i][j] = solve(string, i + 1, j - 1, dp) + 2
    else:
        dp[i][j] = max(solve(string, i + 1, j, dp), solve(string, i, j -1, dp))
    return dp[i][j]

def lps_recur (string):
    n = len(string)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    return solve(string, 0, n-1, dp)

# iterative approach
def lps(string):
    n = len(string)

    dp = [[0 for i in range(n)] for j in range(n)]

    # for string of length of 1 the max length of palindrome is 1
    for i in range(n):
        dp[i][i] = 1
    
    # cl is the length of the substring
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if string[i] == string[j] and cl == 2:
                dp[i][j] = 2
            elif string[i] == string[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return dp[0][n-1]

    
string = "GEEKS FOR GEEKS"
print("Iterative answer {}".format(lps(string)))
print("Recursive answer {}".format(lps_recur(string)))