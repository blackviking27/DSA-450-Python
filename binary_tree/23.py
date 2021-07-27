# Duplicate subtree in Binary Tree

from collections import defaultdict
class Solution:
    def solve(self, root):
        if root is None: # if None then return the marker
            return "$"
        
        s = ""
        # if leaf node
        if root.left is None and root.right is None:
            s += str(root.data)
            return s

        s += str(root.data) # add the current data
        s += self.solve(root.left) # add the left child string
        s += self.solve(root.right) #add the rigth child string 
        
        self.map[s] += 1 # updated the frequency of the string

        return s

    def dupSub(self, root):
        self.map = defaultdict(int)
        self.solve(root)

        for string in self.map:
            if self.map[string] > 1:
                return 1
        return 0
