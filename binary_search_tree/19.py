# Check whether BST contains Dead End 

def find(root, low, high):
    if root is None:
        return False
    
    if low == high: return True

    return find(root.left, low, root.data - 1) or find(root.right, root.data + 1, high)

def deadEnd(root):
    return find(root, 1, float('inf'))