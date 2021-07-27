# Check if all leaf nodes are at same level or not

class Solution:
    def leaf_nodes(self, root, level):
        if root is None: # if node is None return True
            return True
        if root.left is None and root.right is None: # if leaf node
            if self.level == 0: # if the level is not set yet
                self.level = level
                return True # since it is first leaf node
            # if current leaf node level is equal to previous leaf node level or not
            return level == self.level
        
        # if left sub tree has leaf nodes at same level and right sub tree has all leaf nodes at same level
        return self.leaf_nodes(root.left, level + 1) and self.leaf_nodes(root.right, level + 1)
        
    
    def check(self, root):
        self.level = 0 
        ans = self.leaf_nodes(root, 0)
        return ans