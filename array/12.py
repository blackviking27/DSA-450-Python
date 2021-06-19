# Kadane's Algorithm 

class Solution:
    def kadanes_algo(self, arr):
        max_int = float('-inf')
        max_till_here = 0
        for i in range(len(arr)):
            max_till_here += arr[i]
            if max_till_here > max_int:
                max_int = max_till_here
            if max_till_here < 0:
                max_till_here = 0
        
        return max_int