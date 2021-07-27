# Height of Binary Tree

class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        if root is None: # if this the end of a tree
            return 0
        
        max_left = self.height(root.left) # max height of left side
        max_right = self.height(root.right) # max height of right side

        return max(max_left, max_right) + 1