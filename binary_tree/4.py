# Mirror of a binary tree
# https://practice.geeksforgeeks.org/problems/mirror-tree/1

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        if root is None:
            return
        self.mirror(root.left) # moving in left tree till we reach the end
        self.mirror(root.right) # moving in right tree till we reach the end
        root.left, root.right = root.right, root.left