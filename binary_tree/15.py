# Boundary Traversal of binary tree

class Solution:
    def left_tree(self, root, ans): # getting the left boundary elements
        if root is None : return

        if root.left != None: # if left child exists 
            ans.append(root.data)
            self.left_tree(root.left, ans) # call for left child
        elif root.right != None: # if right child exists ans left child does not
            ans.append(root.data)
            self.left_tree(root.right, ans) # call for right child to get next left boundary node
    
    def leaf_nodes(self, root, ans): # getting the leafnodes
        if root is None: return
    
        self.leaf_nodes(root.left, ans) # calling for left child till there is no left child
        
        if root.left is None and root.right is None: # if both left and right child are none then it is the leaf node
            ans.append(root.data)
            
        self.leaf_nodes(root.right, ans) # calling for right child

    def right_tree(self, root, ans): # getting right boundary elements
        if root is None: return

        if root.right != None: # if right child exists then go to the element and don't append yet
            self.right_tree(root.right, ans)
            # after the last right boundary node is reached then we append to answer,
            # so that they are appended in the reversed order
            ans.append(root.data) 
        elif root.left != None:
            self.right_tree(root.left, ans)
            ans.append(root.data)

    def printBoundaryView(self, root):
        if root is None: return []
        
        ans = [root.data] # storing the root data
        self.left_tree(root.left, ans) # starting from the left tree
        self.leaf_nodes(root ,ans) # getting leaf nodes
        self.right_tree(root.right, ans) # starting from right tree
        return ans