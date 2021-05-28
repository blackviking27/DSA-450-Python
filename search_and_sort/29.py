# SUBSUMS - Subset Sums
# Given a sequence of N (1 ≤ N ≤ 34) numbers S1, ..., 
# SN (-20,000,000 ≤ Si ≤ 20,000,000), determine how many subsets of 
# S (including the empty one) have a sum between A and B (-500,000,000 ≤ A ≤ B ≤ 500,000,000), inclusive.

# module to use the bisect_left(lower_bound in c++) 
# and bisect_right(upper_bound in c++)
import bisect

n, a, b = [int(x) for x in input("Enter n, a, b: ").split()]
arr = [1, -2, 3]

# taking the n numbers
for i in range(n):
    arr.append(int(input()))

# this function will add the elements from the index st to ed from the array "arr" to v
# also the function will append sum of all the possible sub arrays from index st to ed
def solve(arr, st, ed, v):
    s = 0
    n = ed - st + 1 # length of the slice of array, from st to ed
    for i in range(2**n):
        s = 0
        j = st
        x = i
        while(x):
            l = x&1
            if l:
                s += arr[j]
            j += 1
            x = x >> 1
        v.append(s)


def total_count(arr, a, b):
    n = len(arr)
    count = 0
    v1 = [] # contains the first half along with the element sums
    v2 = [] # contains the second half which also has the sum of elements

    # assign the right values to the arrays
    solve(arr, 0, (n//2) - 1, v1)
    solve(arr,(n//2), n-1, v2)

    v2.sort()

    for i in range(len(v1)):
        low = bisect.bisect_left(v2, a - v1[i])
        high = bisect.bisect_right(v2, b - v1[i])
        count += high - low
    return count

print(total_count(arr, a, b))

