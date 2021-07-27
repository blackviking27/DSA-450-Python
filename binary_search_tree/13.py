# Brothers From Different Roots

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
'''


def search(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.right, key)
    else:
        return search(root.left, key)

def solve(root1, root2, x, count):
    if root1 is None:
        return
    
    solve(root1.left, root2, x, count)

    key = x - root1.data
    if search(root2, key) is not None:
        count[0] += 1
    
    solve(root1.right, root2, x, count)

def countPairs(root1, root2, x):
    count = [0]
    solve(root1, root2, x, count)
    return count[0]
    