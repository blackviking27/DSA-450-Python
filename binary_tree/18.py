# Transform to Sum Tree

class Solution:
    def toSumTree(self, root) :
        if root is None:
            return 0
        old_val = root.data # storing the old value

        # sum of left sub tree
        lst = self.toSumTree(root.left)
        
        # sum of right sub tree
        rst = self.toSumTree(root.right)
        
        # updating the current value to sum of left sum tee plus right sum tree
        root.data = lst + rst

        # return new value of node plus old value of node to its parent node
        return old_val + root.data