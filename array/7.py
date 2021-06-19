# Kadane's Algorithm
# Given an array arr of N integers. Find the contiguous sub-array with maximum sum

class Solution:
    def max_subarray_sum(self, arr):
        max_int = float('-inf') # getting the smallest number possible
        max_till_here = 0
        for i in range(len(arr)):
            max_till_here += arr[i]
            if max_till_here > max_int:
                max_int = max_till_here
            # when sum is neagative we start from 0 again
            if max_till_here < 0:
                max_till_here = 0
        return max_int
        