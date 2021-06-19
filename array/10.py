# Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number

class Solution:
    def findDuplicate(self, nums):
        num = {} # to keep track of elements
        for el in nums:
            if el in num: # if the element is occuring again
                return el
            else: # element is occuring for the first time
                num[el] = 1