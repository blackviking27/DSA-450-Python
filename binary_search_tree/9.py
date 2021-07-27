# Convert a normal BST to Balanced BST

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def getInorder(self, root):
        if root is not None:
            self.getInorder(root.left)
            self.nodes.append(root)
            self.getInorder(root.right)

    def buildTreeUtil(self, start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        node = self.nodes[mid]

        node.left = self.buildTreeUtil(start, mid - 1)
        node.right = self.buildTreeUtil(mid + 1, end)
        return node
    
    def preOrder(self, root):
        if root is not None:
            print(f"{root.data}", end =" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def buildTree(self, root):
        self.nodes = []
        self.getInorder(root)

        n = len(self.nodes)
        new_root = self.buildTreeUtil(0, n - 1)

        # printing the nodes in preorder
        self.preOrder(new_root)

# Driver code
root = Node(10)
root.left = Node(8)
root.left.left = Node(7)
root.left.left.left = Node(6)
root.left.left.left.left = Node(5)

g = Solution()
g.buildTree(root)