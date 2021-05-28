# Zero Sum Subarrays
# You are given an array arr[] of size n. Find the total count of sub-arrays having their sum equal to 0.

# arr = [int(x) for x in input("Enter the array : ").split()]
from typing import Counter


n = 30
arr = [9, -10, -1, 5, 17, -18, 6, 19, -12, 5, 18, 14, 4, -19, 11, 8, -19, 18, -20, 14, 8, -14, 12, -12, 16, -11, 0, 3, -19, 16]

# using the prefix sum method
def give_counts(arr):
    count = 0
    m = {} # set to know if the sum is recurring
    s = 0 # total sum till that point
    for el in arr:
        s += el
        if s in m:
            count += m[s]
            m[s] += 1
        else:
            if s == 0 and s not in m:
                count += 1
            m[s] = 1
    return count
print(give_counts(arr))

