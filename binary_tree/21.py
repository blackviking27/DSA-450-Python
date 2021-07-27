# Sum Tree 
# Given a Binary Tree. Return 1 if, for every node X in the tree other than the leaves,
# its value is equal to the sum of its left subtree's value and its right subtree's value. Else return 0

class Solution:
    def sum_tree(self, root):
        if root is None:
            return 0
        # if leaf node is present then return the data
        if root.left is None  and root.right is None: return root.data
        
        # if already at some point it is false then we need not check again
        if self.sum == False: return False
        
        a = self.sum_tree(root.left)
        b = self.sum_tree(root.right)
        if a + b != root.data: self.sum = False # if sum of left  sub tree and right sub tree is not equal to node value then it is not a sum tree
        
        return a + b + root.data
    
    def isSumTree(self,root):
        self.sum = True # global variable of object to tell if tree is sum tree or not
        res = self.sum_tree(root)
        return self.sum