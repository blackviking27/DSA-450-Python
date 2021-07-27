#  Maximum difference of zeros and ones in binary string 

class Solution:
    def maxSubstring(self, S):
        arr = [] # stores the values, if 0 then 1 and if 1 then  -1
        for char in S:
            if char == '1':
                arr.append(-1)
            else:
                arr.append(1)
        
        # using kadanes algorigthm to find the max sum of contigous subarray
        max_total = float('inf')
        max_sofar = 0
        
        for i in range(len(arr)):
            max_sofar += arr[i]

            # updating the global max
            max_total = max(max_total, max_sofar)

            # if max_sofar is negative then make it 0
            if max_sofar < 0:
                max_sofar = 0
        return max_total