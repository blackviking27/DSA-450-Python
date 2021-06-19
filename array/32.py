# Minimum swaps and K together 
# Given an array of n positive integers and a number k. 
# Find the minimum number of swaps required to bring all the numbers less than or equal to k together.

def minSwao(arr, n, k):
    count = 0 # counts the number of elements less than or equal to k
    for i in range(n):
        if arr[i] <= k:
            count += 1
    
    bad = 0 # keeps the count of elements greater than k in window of 'count' size
    for i in range(count):
        if arr[i] > k:
            bad += 1
    
    # moving the window of size 'k' to see the min swaps
    i = 0 # starting index of window
    j = count - 1 # last index of window

    mi = float('inf') # minimum no of swaps

    while  j < n:
        mi = min(mi, bad)
        j += 1
        if j < n:
            if arr[j] > k: bad += 1
        if i < n:
            if arr[i] > k: bad -= 1
        i += 1
    return mi if mi < float('inf') else 0
