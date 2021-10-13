# Minimum sum
# Given an array Arr of size N such that each element is from the range 0 to 9.
# Find the minimum possible sum of two numbers formed using the elements of the array.
# All digits in the given array must be used to form the two numbers.

import heapq


class Solution:
    def solve(self, arr, n):
        num1 = ""
        num2 = ""

        heapq.heapify(arr)

        # if 0, then add the current digit to num1
        # if 1, then add the current digit to num2
        bi = 0

        while arr:
            if bi == 0:
                num1 += str(heapq.heappop(arr))
                bi = 1
            else:
                num2 += str(heapq.heappop(arr))
                bi = 0
        return (int(num1) if len(num1) != 0 else 0) + (int(num2) if len(num2) != 0 else 0)
