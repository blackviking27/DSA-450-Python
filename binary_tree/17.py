# Binary Tree to DLL


'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
class dll:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

def bToDLL(root):
    inorder = [] # stores the inorder traversal
    stack = [] 

    # finding the inorder traversal of a tree in a iterative manner
    curr = root
    while curr or stack:
        if curr != None:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            inorder.append(curr.data)
            curr = curr.right
    
    # constructing the dll with the given inorder traversal
    head = dll(inorder[0])
    curr = head
    for i in range(1, len(inorder)):
        temp = dll(inorder[i])
        curr.right = temp
        temp.left = curr
        curr = temp
    return head