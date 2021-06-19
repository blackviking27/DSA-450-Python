# Minimum number of jumps
# Given an array of N integers arr[] where each element represents 
# the max number of steps that can be made forward from that element. 
# Find the minimum number of jumps to reach the end of the array (starting from the first element). 
# If an element is 0, then you cannot move through that element.

class Solution:
    def minJumps(self, arr, n):
        mr = arr[0] # max reach
        step = arr[0]
        jumps = 1
        if n==1: return 0
        elif arr[0] == 0: return -1
        else:
            for i in range(1, n):
                if i == n - 1:
                    return jumps
                mr = max(mr, arr[i] + i)
                step -= 1
                if step == 0:
                    jumps += 1
                    if i >= mr:
                        return -1
                    step = mr - i

