# Flatten BST to sorted list | Increasing order

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


class Solution:
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.prev.left = None
        self.prev.right = root
        self.prev = root
        self.inorder(root.right)

    def flatten(self, root):
        dummy = Node(-1)
        self.prev = dummy
        self.inorder(root)
        # print(prev.data)
        self.printTree(dummy.right)

    def printTree(self, root):
        if root is None:
            return
        self.printTree(root.left)
        print(root.data, end=" ")
        self.printTree(root.right)

# Driver code
root = Node(5);
root.left = Node(3);
root.right = Node(7);
root.left.left = Node(2);
root.left.right = Node(4);
root.right.left = Node(6);
root.right.right = Node(8);

bst = Solution()
bst.flatten(root)