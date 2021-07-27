# Word break

def solve(string, words, dp):
    n = len(string)

    # if length is zero
    if n == 0: return 1

    # if alerady caculated
    if dp[string] != 0: return dp[string]

    #  taking the first sub string
    for i in range(n):
        f = 0 # to determine if we find the substring in words or not
        sub_str = string[:i] # taking the substring

        # going through each word
        for j in range(len(words)):
            if words[i] == sub_str:
                f = 1 # if we find the word
                break
        # if we find the current substring and the rest of the sub strings too
        if f == 1 and solve(string[i:], words, dp) == True: 
            dp[string] = True
            return dp[string]

    dp[string] = False
    return dp[string]
    
from collections import defaultdict
def wordBreak(line, dictionary):
    dp = defaultdict(int)
    x = solve(line, dictionary, dp)
    return x

