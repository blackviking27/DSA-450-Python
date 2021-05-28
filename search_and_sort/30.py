# Count Inversions
# Given an array of integers. Find the Inversion Count in the array. 
# Inversion Count: For an array, inversion count indicates how far (or close) 
# the array is from being sorted. If array is already sorted then the inversion count is 0. 
# If an array is sorted in the reverse order then the inversion count is the maximum. 
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.


# merge function
def merge(arr, temp, left, mid, right):
    i = left # first index of left subarray
    j = mid + 1 # first index of right subarray
    k = left # index of sorted subarray
    inv = 0 # count of inversions

    # merging the two subarray
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            # inversion occured
            inv += mid - i + 1
            temp[k] = arr[j]
            j += 1
            k += 1
    
    # adding the remainig elements
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # copying the elements in the original array
    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv

# merge sort function
def merge_sort(arr, temp, left, right):
    inv = 0
    if left < right:
        mid = (left + right) // 2
        inv += merge_sort(arr, temp, left, mid) # taking the left subarray
        inv += merge_sort(arr, temp, mid + 1, right) # taking the right subarray
        inv += merge(arr, temp, left, mid, right) # merging both the subarray
    return inv

def inv_count(arr):
    n = len(arr)
    temp = [0]*n
    result = merge_sort(arr, temp, 0, n -1)
    return result