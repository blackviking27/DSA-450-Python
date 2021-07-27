# LargestSum Contiguous Subarray [V>V>V>V IMP ]

class Solution:
    def largestSumSubarray(self, arr, n):

        max_sum = float('-inf') # max sum
        max_till_here = 0 # max till the current element

        for i in range(n):
            max_till_here += arr[i]
            max_sum = max(max_sum, max_till_here)

            if max_till_here < 0:
                max_till_here = 0
        return max_sum
