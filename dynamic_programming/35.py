# 	Smallest sum contiguous subarray

def smallestSumSubarr(arr, n):
    min_sum = float('inf')
    min_till_here = float('inf')

    for i in range(n):
        if min_till_here > 0:
            min_till_here = arr[i]
        else:
            min_till_here += arr[i]
        
        min_sum = min(min_sum, min_till_here)
    
    return min_sum

arr = [3, -4, 2, -3, -1, 7, -5]
n = len(arr)
print(smallestSumSubarr(arr, n))