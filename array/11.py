# Merge Without Extra Space
# Given two sorted arrays arr1[] of size N and arr2[] of size M. 
# Each array is sorted in non-decreasing order. Merge the two arrays into 
# one sorted array in non-decreasing order without using any extra space

class Solution:
    def merge(self, arr1, arr2, n, m):
        def next_gap(gap):
            if gap > 1:
                return (gap // 2) + (gap % 2) # taking the upper bound
            else:
                return 0

        gap = next_gap(n + m) # intial gap
        while gap > 0:

            # for the first array
            i = 0
            while i + gap < n:
                if arr1[i] > arr1[i + gap]: # moving the smaller one
                    arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
                i += 1
            
            # traversing both first and seconf array
            j = gap - n if gap > n else 0 # if gap > n that means the j index starts at some point in the second array
            while i < n and j < m:
                if arr1[i] > arr2[j]:
                    arr1[i], arr2[j] = arr2[j], arr1[i]
                i += 1
                j += 1
            
            # traversing the second arry if end of second array if not reached
            if j < m:
                j = 0
                while j + gap < m:
                    if arr2[j] > arr2[j + gap]:
                        arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                    j += 1

            gap = next_gap(gap)