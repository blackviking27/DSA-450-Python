# k-th smallest element in BST 

# using inorder traversal

class Solution:
    def find(self, root, k):
        if root is None or self.c >= k:
            return
        
        self.find(root.left, k)

        self.c += 1
        if self.c == k:
            self.ans = root.data
            return
        
        self.find(root.right, k)

    def KthSmallestElement(self, root, K):
        self.ans = -1
        self.c = 0
        self.find(root, K)
        return self.ans 