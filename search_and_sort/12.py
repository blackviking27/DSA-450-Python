# Count triplets with sum smaller than X
#Given an array arr[] of distinct integers of size N and a sum value X, 
# the task is to find count of triplets with the sum smaller than the given sum value X.

l, x = input("Enter l, x: ").split()
arr = [int(x) for x in input("Enter array: ").split()]

def give_triplets(arr, x):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            if arr[left] + arr[right] + arr[i] < x:
                count += right - left
                left += 1
            else:
                right -= 1
    return count
print(give_triplets(arr, x))