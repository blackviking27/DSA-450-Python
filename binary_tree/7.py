# Postorder Traversal of a tree both using recursion and Iteration

from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def postorder_recur(self, root):
        if root is None:
            return
        self.postorder_recur(root.left)
        self.postorder_recur(root.right)
        print(root.data, end=" ")
    
    def postorder_itr(self, root):
        stack = deque()
        stack.append(root)
        ans = deque()
        while stack:
            curr = stack.pop()
            ans.append(curr.data)
            if curr.left != None: stack.append(curr.left)
            if curr.right != None: stack.append(curr.right)
        while ans:
            print(ans.pop(), end=" ")

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
solution.postorder_recur(root)
print()
solution.postorder_itr(root)
