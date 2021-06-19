# Array Subset of another array 
# Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. 
# Task is to check whether a2[] is a subset of a1[] or not. 
# Both the arrays can be sorted or unsorted. 
# It may be assumed that elements in both array are distinct.

def isSubset( a1, a2, n, m):
    count = {}
    for i in range(n):
        count[a1[i]] = 1
    c = 0
    for i in range(m):
        if a2[i] in count:
            c += 1
    
    return "Yes" if c == m else "No"