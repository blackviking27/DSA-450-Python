# Count the Reversals 
# Given a string S consisting of only opening and closing curly brackets '{' and '}', 
# find out the minimum number of reversals required to convert the string into a balanced expression.
# A reversal means changing '{' to '}' or vice-versa.

import math
def countRev(s):    
    
    n = len(s)

    # for odd length it is not possible to pair every bracket as one will be left every time
    if n % 2 != 0:
        return -1

    open_bracket = 0 # count of close bracket
    close_bracket = 0 # count of close bracket

    for i in range(n):
        if s[i] == '{':
            open_bracket += 1 # counting open brackets
        else:
            if open_bracket != 0: # checking if an open bracket exists or not for current closing bracket
                open_bracket -= 1
            else: # when no open bracket exists
                close_bracket += 1
    
    return math.ceil(open_bracket / 2) + math.ceil(close_bracket / 2)