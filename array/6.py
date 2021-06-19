# Cyclically rotate an array by one 
# Given an array, rotate the array by one position in clock-wise direction.

def rotate( arr, n):
    last = arr[n-1] # taking the last element
    for i in range(n-2, -1, -1): # moving from second last to first
        arr[i + 1] = arr[i] # copying the current value to its next value
    arr[0] = last # placing the last element at first
    return arr