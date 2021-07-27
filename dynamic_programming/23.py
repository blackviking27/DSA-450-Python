# Max length chain

"""
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
"""

def maxChainLen(arr, n):

    # sorting the array according to the first element
    arr.sort(key= lambda x: x.a) # sorting the array
    
    # stores the max length of chain till that index, following the longest increasing subsequence approach
    dp =[1 for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[i].a > arr[j].b:
                dp[i] = max(dp[i], dp[j] + 1)
    
    max_len = 0
    for i in range(n):
        max_len = max(max_len, dp[i])
    return max_len