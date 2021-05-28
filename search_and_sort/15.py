# Product array puzzle
# Given an array nums[] of size n, construct a Product Array P (of same size n) 
# such that P[i] is equal to the product of all the elements of nums except nums[i].

# arr = [int(x) for x in input("Enter the array : ").split()]
arr = [10, 3, 5, 6, 2]

# Given we cannot use the division operator
def puzzle_product(arr):
    n = len(arr)
    res = []
    l = [0]*n
    r = [0]*n
    l[0] = 1
    r[n-1] = 1
    # assigning values in the left and right arrays
    for i in range(1, n):
        l[i] = l[i - 1] * arr[i - 1]
    for i in range(n-2, -1, -1):
        r[i] = r[i + 1] * arr[i + 1]

    for i in range(n):
        res.append(l[i] * r[i])
    return res

print(*puzzle_product(arr))