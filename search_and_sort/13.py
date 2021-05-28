# Merge Without Extra Space
# Given two sorted arrays arr1[] of size N and arr2[] of size M. 
# Each array is sorted in non-decreasing order. 
# Merge the two arrays into one sorted array in non-decreasing order without using any extra space.

arr1 = [int(x) for x in input("Enter array 1: ").split()]
arr2 = [int(x) for x in input("Enter array 2: ").split()]

# using the deafult method
def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    for i in range(m-1, -1, -1):
        last = arr1[n-1]
        j = n - 2
        while j >= 0 and arr1[j] > arr2[i]:
            arr1[j + 1] = arr1[j]
            j -= 1
        if j != n - 2 or last > arr2[i]:
            arr1[j + 1] = arr2[i]
            arr2[i] = last
    return arr1, arr2

# Using the gap method
def next_gap(gap):
    if gap > 1:
        return (gap // 2) + (gap % 2)
    else:
        return 0
def gap_merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)   
    gap = next_gap(n + m)

    while gap > 0:
        # traversing the first array
        i = 0
        while i + gap < n:
            if arr1[i]  > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1
        
        # traversing between the array
        j = gap - n if gap > n else  0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        
        # traversing the second array if need j < m
        if (j < m):
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1
        
        gap = next_gap(gap)

