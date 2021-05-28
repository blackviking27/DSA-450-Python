# In-Place Merge Sort
# Implement Merge Sort i.e. standard implementation keeping the sorting algorithm as in-place. 
# In-place means it does not occupy extra memory for merge operation as in the standard case.

def merge(arr, start, mid, end):
    # start is the first index of the first array
    start2 = mid + 1 # starting index of the second array

    # if both the subarrays are already sorted
    if arr[mid] <= arr[start2]:
        return

    while start <= mid and start2 <=end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            while  index != start:
                arr[index] = arr[index - 1]
                index -= 1
            
            arr[start] = value


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)