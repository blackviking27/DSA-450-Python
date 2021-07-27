# Level order traversal 
# Given a binary tree, find its level order traversal.
# Level order traversal of a tree is breadth-first traversal for the tree.

from collections import deque

class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        stack = deque() # stores the child node
        stack.append(root)
        ans = []
        while len(stack) != 0:
            first = stack.popleft() # removing the first node
            if first != None: # if we have a valid node or not
                stack.append(first.left)
                stack.append(first.right)
                ans.append(first.data)
        return ans
            
        