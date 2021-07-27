# Lowest Common Ancestor in a Binary Tree

class Solution:
    def lca(self,root, n1, n2):
        if root is None:
            return None
        
        if root.data == n1 or root.data == n2: return root

        left_node = self.lca(root.left, n1, n2)
        right_node = self.lca(root.right, n1, n2)

        # if both sides are not None then the current node is LCA
        if left_node != None and right_node != None: return root

        if left_node:
            return left_node
        else:
            return right_node
