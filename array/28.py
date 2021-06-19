# Trapping Rain Water 
# Given an array arr[] of N non-negative integers representing the height of blocks. 
# If width of each block is 1, compute how much water can be trapped between the blocks 
# during the rainy season.

class Solution:
    def trap(self, arr, n):
        l = [0]*n
        r = [0]*n

        ans = 0 # water trapped
        
        max_left = l[0] = arr[0] # max height from left
        max_right = r[n - 1] = arr[n - 1] # max height from right

        # calculating the maximum height from left till that poistion
        for i in range(1, n):
            if max_left < arr[i]:
                max_left = arr[i]
            l[i] = max_left
        
        # calculating the maximum height from right till that poistion
        for i in range(n-2, -1, -1):
            if max_right < arr[i]:
                max_right = arr[i]
            r[i] = max_right
        
        for i in range(n):
            ans += min(l[i], r[i]) - arr[i]

        return ans
    
    # without extra space
    def trap2(self, arr, n):
        ml = mr = 0
        lo = 0 # starting of array
        hi = n - 1 # ending of array
        ans = 0
        while lo <= hi:
            # for left side
            if arr[lo] <= arr[hi]:
                if arr[lo] > ml:
                    ml = arr[lo]
                else:
                    ans += ml - arr[lo]
                lo += 1
            else:
                if arr[hi] > mr:
                    mr = arr[hi]
                else:
                    ans += mr - arr[hi]
                hi -= 1
        return ans