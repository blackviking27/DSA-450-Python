# Smallest subarray with sum greater than x
# Given an array of integers (A[])  and a number x, 
# find the smallest subarray with sum greater than the given value.

class Solution:
    def sb(self, arr, n, x):
        min_len = n + 1
        curr_sum = 0

        i = 0 # starting index of the subarray
        j = 0 # ending index of the subarray

        while i <= j and  j < n:
            # finding the sub array whose sum is less than or eqaul to X
            while curr_sum <= x and j < n:
                curr_sum += arr[j]
                j += 1
            
            # find another subarray whose sum is less than or greater to x
            # and is shorter than the current array
            while curr_sum > x and i <j:
                min_len = min(min_len, j - i)
                curr_sum -= arr[i]
                i += 1
        return min_len