# Merge Two Balanced Binary Search Trees

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
    
def insert( root, key):
    if root is None:
        return Node(key)
        
    if root == key:
        return root
    elif root.data < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

class Solution:
    def mergeInorderArr(self, arr1, arr2):
        res = []
        i = j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i].data <= arr2[j].data:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        while i < len(arr1):
            res.append(arr1[i])
            i += 1

        while j < len(arr2):
            res.append(arr2[j])
            j += 1
        return res

    def getInorder(self, root, arr):
        if root is not None:
            self.getInorder(root.left, arr)
            arr.append(root)
            self.getInorder(root.right, arr)

    def createBalancedBST(self, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        node = self.res_inorder[mid]

        node.left = self.createBalancedBST(start, mid - 1)
        node.right = self.createBalancedBST(mid + 1, end)

        return node

    def printTree(self, root):
        if root:
            self.printTree(root.left)
            print(f"{root.data}", end=" ")
            self.printTree(root.right)

    def mergeTwoBST(self, root1, root2):
        inorder1 = []
        inorder2 = []
        self.getInorder(root1, inorder1)
        self.getInorder(root2, inorder2)

        self.res_inorder = self.mergeInorderArr(inorder1, inorder2)

        n = len(self.res_inorder)
        new_root = self.createBalancedBST(0, n - 1)
        self.printTree(new_root)
        

# driver code
root1 = root2 = None

# Inserting values in first tree
root1 = insert(root1, 100)
root1 = insert(root1, 50)
root1 = insert(root1, 300)
root1 = insert(root1, 20)
root1 = insert(root1, 70)
     
# Inserting values in second tree
root2 = insert(root2, 80)
root2 = insert(root2, 40)
root2 = insert(root2, 120)

bst = Solution()

bst.mergeTwoBST(root1, root2)