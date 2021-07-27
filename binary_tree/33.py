# Duplicate Subtrees

from collections import defaultdict
class Solution:
    def inorder(self, root):
        if root is None:
            return ""
        
        # to create the unique subtrees
        s = "("
        s += self.inorder(root.left)
        s += str(root.data)
        s += self.inorder(root.right)
        s += ")"
        
        if s in self.map and self.map[s] == 1: # if already present in the map then just add node to answer
            self.res.append(root) 
        self.map[s] += 1 # increase the occurence
        return s
        
    def printAllDups(self,root):
        self.map = defaultdict(int) # to store the occurence of strings
        self.res = []
        self.inorder(root)
        return self.res