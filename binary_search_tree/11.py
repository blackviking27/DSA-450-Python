# 	Find Kth largest element in a BST

# using reverse inorder traversal

class Solution:
    def find(self, root, k):
        if root is None or self.c >= k:
            return
        
        # moving to right
        self.find(root.right, k)
        self.c += 1
        if self.c == k:
            self.ans = root.data
            return
        # moving to left
        self.find(root.left, k)

    def findKthLargest(self, root, k):
        self.c = 0
        self.ans = 0
