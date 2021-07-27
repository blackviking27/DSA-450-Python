# Right View of Binary Tree 

from collections import deque
def rightView(root):

    if root is None: return [] # if root node is empty

    q = deque([root])
    ans = []
    while len(q) != 0:
        n = len(q)
        temp = None
        for _ in range(n):
            temp = q.popleft() # removing the element from the same level
            if temp.left: q.append(temp.left)
            if temp.right: q.append(temp.right)
        ans.append(temp.data) # adding the last popped element in the level
    return ans