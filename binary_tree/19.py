# Construct Tree from Inorder & Preorder

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None        
        self.right = None

class Solution:
    def create_tree(self, inorder, preorder, in_start, in_end):
        if in_start > in_end:
            return None
        
        # taking current element from preorder
        curr = preorder[self.preIdx]
        self.preIdx += 1 # pointing to the next element in preorder
        temp = Node(curr) # creating a node for current value
        
        if in_start == in_end: # if no left and right child is left
            return temp
        
        # element to the left of this index will be in left sub tree of current node
        # element to the right if this index will be in right sub tree of current node 
        inIdx = self.mp[curr] 
        
        # taking the left subtree
        temp.left = self.create_tree(inorder, preorder, in_start, inIdx - 1)

        # taking the right sub tree
        temp.right = self.create_tree(inorder, preorder, inIdx + 1, in_end)
        return temp
        
    def buildtree(self, inorder, preorder, n):
        self.mp = {} # mapping the element to index of inorder
        for i in range(len(inorder)):
            self.mp[inorder[i]] = i
        self.preIdx = 0 # index of preorder
        return self.create_tree(inorder, preorder, 0 , len(inorder) - 1)