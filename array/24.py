# Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# easy solution -> use a map to keep count of each element then check if they occur more tha floor(n/3) times
# Question problem

class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        num1 = 0
        num2 = 0
        c1 = 0
        c2 = 0
        for i in range(n):
            if nums[i] == num1:
                c1 += 1
            elif nums[i] == num2:
                c2 += 1
            elif c1 == 0:
                num1 = nums[i]
                c1 = 1
            elif c2 == 0:
                num2 = nums[i]
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        ans = []
        c1 = c2 = 0
        for i in range(n):
            if nums[i] == num1:
                c1 += 1
            elif nums[i] == num2:
                c2 += 1
        
        if c1 > n //3:
            ans.append(num1)
        if c2 > n //3:
            ans.append(num2)
        
        return ans
        