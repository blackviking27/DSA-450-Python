# Binary Tree to BST

class Solution:
    def getInorder(self, root):
        if root:
            # moving to the left sub tree
            self.getInorder(root.left)

            # appending the data to the list
            self.inorder.append(root.data)
            
            # moving to right sub tree
            self.getInorder(root.right)

    def convert(self, root):
        if root:
            self.convert(root.left)

            # appending the elements
            root.data = self.inorder.pop(0)
            
            self.convert(root.right)

    def binaryTreeToBST(self, root):
        # stores the inorder traversal of binary tree
        self.inorder = []
        self.getInorder(root)

        # sorting the inorder since in BST the inorder traversal is sorted
        self.inorder.sort()

        # traversing in inorder and updating the values according to the sorted values
        self.convert(root)

        return root