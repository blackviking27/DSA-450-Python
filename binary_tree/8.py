# Left View of a tree

from collections import deque
def leftView(root):
    if root is None: # if empty node is given
        return []
    
    q = deque()
    q.append(root)
    ans = []
    while len(q) != 0:
        n = len(q) # taking the len which gives the number of node in current level

        for i in range(n):
            temp = q.popleft() # taking the left most element
            if i == 0: # if it is the first element then append to answer
                ans.append(temp.data)
            if temp.left != None: q.append(temp.left) # adding its left node
            if temp.right != None: q.append(temp.right) # adding its right node
    return ans