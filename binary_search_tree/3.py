# Find inorder successor and inorder predecessor in a BST

class Node:
    def __init__(self, key) -> None:
        self.key = key 
        self.right = None
        self.left = None


def inorderPredecessor(self, root):
    curr = root
    while root.right is not None:
        curr = curr.right
    return curr

def inorderSucessor(self, root):
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr

def findPredSucc(root, pred, succ, key):
    if root is None:
        return
    
    if root.key == key:
        if root.left:
            pred = inorderPredecessor(root.left) 
        
        if root.right:
            succ = inorderSucessor(root.right)
        
        return
    
    elif key > root.key:
        pred = root
        findPredSucc(root.right, pred, succ, key)
    
    else:
        succ = root
        findPredSucc(root.left, pred, succ, key)

