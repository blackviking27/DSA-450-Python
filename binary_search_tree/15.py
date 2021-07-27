# 	Count BST ndoes that lie in a given range

# O(n) approach
def count(root, low, high, c):
    if root is None:
        return
    count(root.left, low, high, c)
    if root.data in range(low, high + 1):
        c[0] += 1
    
    count(root.right, low, high, c)

def getCount(root,low,high):
    c = [0]
    count(root, low, high, c)
    return c[0]

# better than O(n) approach, still O(n) though
def getCount(root, low, high):
    if root is None:
        return 0
    
    if root.data >= low and root.data <= high:
        return 1 + getCount(root.left, low, high) + getCount(root.right, low, high)
    elif root.data < low:
        return getCount(root.right, low, high)
    else:
        return getCount(root.left, low, high)