# Check if a tree is a BST or not

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None

class Solution:
    def isBSTUtil(self, root, mi, ma):
        # empty tree is a BST
        if root is None:
            return True
        
        # root data lies outide the given range
        if root.data < mi or root.data > ma:
            return False
        
        return self.isBSTUtil(root.left, mi, root.data - 1) and self.isBSTUtil(root.right, root.data + 1, ma)

    def isBST(self, root):
        max_int = float('inf')
        min_int = float('-inf')
        return self.isBSTUtil(root, min_int, max_int)

    
    # check for BST with inorder traversal
    def inorderBST(self, root):
        if root is None: return

        self.inorderBST(root.left)
        if self.prev != None and self.prev.data >= root.data:
            self.flag = False
            return

        self.prev = root
        self.inorderBST(root.right)

    def isBSTInorder(self, root):
        self.flag = True
        self.prev = None
        self.inorderBST(root)
        return self.flag
