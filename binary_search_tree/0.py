# search and insertiion in binary search tree

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

# Search in a BST
def search(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.right, key)
    return search(root.left, key)

# Insert in a BST
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)