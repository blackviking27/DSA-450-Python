# Largest Independent Set Problem

# setting up the node value
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.liss = 0 # stores the max length of Longest Independent set Problem

def liss(root):
    if root == None:
        return 0
    
    if root.liss != 0:
        return root.liss
    
    if root.left == None and root.right == None:
        root.liss = 1
        return root.liss
    
    # exluding the current node
    size_excl = liss(root.left) + liss(root.right)

    # including the current nod
    size_incl = 1
    if root.left != None:
        size_incl += (liss(root.left.left) + liss(root.left.right))
    if root.right != None:
        size_incl += (liss(root.right.left) + liss(root.right.right))
    
    root.liss = max(size_incl, size_excl)
    return root.liss

# Driver Code
root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)
root.right = node(22)
root.right.right = node(25)

print("LIS is", liss(root))