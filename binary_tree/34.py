

class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def isIsomorphic(self, root1, root2): 
        # empty trees are isomorphic
        if root1 is None and root2 is None:
            return True
        
        # if either of them is none then we cannot obtain the other
        if root1 is None or root2 is None:
            return False
        
        #  if both nodes have different value
        if root1.data != root2.data:
            return False
        
        # if left sub trees of both nodes are isomorphic or not
        # if right sub trees of both nodes are isomorphic or not
        l1 = self.isIsomorphic(root1.left, root2.left) and self.isIsomorphic(root1.right, root2.right)

        # if left and right sub tree of nodes is isomorphic or not
        # if right and left sub tree of nodes is isomorphic or not
        l2 = self.isIsomorphic(root1.left, root2.right) and self.isIsomorphic(root1.right, root2.left)
        
        return l1 or l2