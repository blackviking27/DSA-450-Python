# Longest consecutive subsequence
# Given an array of positive integers. 
# Find the length of the longest sub-sequence such that elements in the 
# subsequence are consecutive integers, the consecutive numbers can be in any order.


class Solution:
    def longest(self, arr, N):
        s = set()
        ans = 0
        for el in arr:
            s.add(el)
        for i in range(N):
            if arr[i] - 1 not in s:
                j = arr[i]
                while j in s:
                    j += 1

                ans = max(ans, j - arr[i])
        return ans