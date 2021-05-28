# Searching in an array where adjacent differ by at most k

arr = [int(x) for x in input("Enter array : ").split()]
k = int(input("Enter k : "))
x = int(input("Enter x : "))

def search(arr, k, x):
    i = 0
    while i < len(arr):
        if arr[i] == x:
            return i
        
        # incrementing value of i
        i += max(1, int(abs(arr[i] - x)/k))
    return -1