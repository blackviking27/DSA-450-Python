# Sum of the Longest Bloodline of a Tree

class Solution:
    def solve(self,root):
        if root is None: # if none then return
            return [0, 0] # returns level, sum as 0, 0
        
        a = self.solve(root.left) # taking the left sub tree
        b = self.solve(root.right) # taking the right sub tree
        
        if a[0] > b [0]: # if level of left is greater then take that into sum
            return [a[0] + 1, a[1] + root.data]
        elif a[0] < b[0]: # if  level of right is greater then take that into sum
            return [b[0] + 1, b[1] + root.data]
        else: # if both level are equal then consider the max sum till that level
            return [a[0] + 1, max(a[1], b[1]) + root.data]
        
    
    def sumOfLongRootToLeafPath(self,root):
        ans = self.solve(root)
        return ans[1]