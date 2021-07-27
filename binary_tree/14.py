# Diagonal Traversal of Binary Tree
# question link => Diagonal Traversal of Binary Tree

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque

def diagonal(root):
    q = deque([root]) # this queue stores the left node of the current node
    ans = []

    while len(q) != 0:
        temp = q.popleft() # taking the first element in the next diagonal 
        while temp != None: # moving in the right direction till there is no right childe
            ans.append(temp.data)
            if temp.left != None: # if left child exists then add it to the queue since it will in the next column
                q.append(temp.left)
            temp = temp.right
    return ans