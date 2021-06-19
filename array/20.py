# Subarray with 0 sum 
# Given an array of positive and negative numbers. 
# Find if there is a subarray (of size at-least one) with 0 sum.

class Solution:
    def subArrayExists(self, arr, n):
        f = 0
        m = {} # contains the map of prefix sums
        s = 0 # prefix sum
        for i in range(len(arr)):
            s += arr[i]
            # if prefix sum is zero or the sum is recurring
            # of the array element itself is zero then a 
            # sub array exists
            if s == 0 or s in m or arr[i] == 0:
                f = 1
                break
            else:
                m[s] = 1
        return True if f == 1 else False