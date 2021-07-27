# Inorder Traversal of a tree both using recursion and Iteration

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def inorder_recur(self, root):
        if root is None:
            return
        self.inorder_recur(root.left) # moving to the left subtree
        print(root.data, end=" ") # the current node
        self.inorder_recur(root.right) # mocing to the right sub tree
    
    def inorder_itr(self, root):
        stack = deque()
        curr = root
        res = []
        # if stack is empty and curr node is none then we no longer need to traverse the tree
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left # moving to the left
            else:
                curr = stack.pop() # taking the element at top
                res.append(curr.data)
                curr = curr.right  # moving to the right subtree
        print(*res) # printing the result

# Driver code

""" Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

solution = Solution()
solution.inorder_recur(root)
print()
solution.inorder_itr(root)