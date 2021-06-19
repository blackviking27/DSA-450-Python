# Wildcard Pattern Matching

def match(pattern, string):
    # n,m are length of the string and pattern respectively
    n = len(string)
    m = len(pattern)
    if m == 0:
        return n == 0

    # maintains th  result for string length of m and n
    dp = [[False for i in range(m + 1)] for j in range(n + 1)]

    # empty string and pattern are true
    dp[0][0] = True

    # * can match a empty string
    for j in range(1, m + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # filliing the table
    for i in range(1, n +1):
        for j in range(1, m + 1):
            # i, j are lengths of the string and pattern
            # we encounter '*' then we can either ignore it or consider it
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            # the two characters of pattern and string match when
            #  we have the same character of pattern has '?'
            elif pattern[ j - 1] == '?' or pattern[j -1] == string[i -1]:
                dp[i][j] = dp[i - 1][j - 1]
            # when they don't match
            else:
                dp[i][j] = False
    return dp[n][m]