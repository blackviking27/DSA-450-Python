# Preorder Traversal of a tree both using recursion and Iteration

from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def preorder_recur(self, root):
        if root is None:
            return
        print(root.data, end =" ")
        self.preorder_recur(root.left)
        self.preorder_recur(root.right)
    
    def preorder_itr(self, root):
        stack = deque()
        ans = []
        stack.append(root) # inserting the root element at top
        # while the stack is not empty
        while stack:
            curr = stack.pop() # taking the top element
            ans.append(curr.data)

            # curr.right is pushed first so that curr.left is at the top for the next iteration
            if curr.right != None: stack.append(curr.right)
            if curr.left != None: stack.append(curr.left)
        
        print(*ans)

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
solution.preorder_recur(root)
print()
solution.preorder_itr(root)