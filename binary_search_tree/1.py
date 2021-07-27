# 	Deletion of a node in a BST


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None


class Solution:

    def inorderSucc(self, root):
        curr = root
        while curr.left !=  None:
            curr = curr.left
        return curr

    def deleteNode(self, root, key):
        if root is None:
            return 
        
        # finding the key in the BST
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.right is None:
                temp = root.left
                root = None
                return temp
            
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            # when both left and right subtree exists
            temp = self.inorderSucc(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)