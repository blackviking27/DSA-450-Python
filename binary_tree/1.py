# Reverse Level Order Traversal
# Given a binary tree of size N, find its reverse level order traversal. ie- the traversal must begin from the last level

from collections import deque

def reverseLevelOrder(root):
    q = deque() # for getting the order
    q.append(root)
    ans = deque()
    while len(q) != 0:
        node = q.popleft() # getting the first element
        
        if node != None:
            ans.appendleft(node.data) # appending the current node data at the beginning of the ans queue
            
            # inserting the right node first so that when we append the node to ans we get the
            # left node before right node
            if node.right != None: q.append(node.right) 
            if node.left != None: q.append(node.left)
    return ans