# Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping 
# ntervals that cover all the intervals in the input.

class Solution:
    def merge(self, arr):
        # contains the intervals
        arr.sort() # sorting the array according to the start of the range in each interval
        idx = 0 # keeps track of the latest merged interval
        for i in range(1, len(arr)):
            # if the start time of the ith index is less than the end time
            # of the last merged interval, if true then merges the two intervals
            if arr[idx][1] >= arr[i][0]:
                arr[idx][1] = max(arr[idx][1], arr[i][1])
            else:
                # if we cannot merge then we move to the next index and copy the next interval there
                idx += 1
                arr[idx] = arr[i]
        
        return arr[:idx + 1]