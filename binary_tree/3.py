# Diameter of Binary Tree 

class Height:
    def __init__(self):
        self.h = 0

class Solution:
    def diameterOpt(self, root, height):
        lh = Height() # height of left sub tree
        rh = Height() # height of right sub tree
        if root is None:
            height.h = 0
            return 0
        
        ld = self.diameterOpt(root.left, lh) # taking the left diameter
        rd = self.diameterOpt(root.right, rh) # taking the right diameter
        
        height.h = max(lh.h, rh.h) + 1 # max of left and right height  + 1
        return max(lh.h + rh.h + 1, max(ld, rd))
            
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        height = Height()
        return self.diameterOpt(root, height)