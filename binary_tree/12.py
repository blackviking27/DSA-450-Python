# ZigZag Tree Traversal

from collections import deque
def zigZagTraversal(root):
    if root is None: return []

    curr_level = deque([root]) # stores the node in current level
    next_level = deque([]) # stores the node in next level

    reverse = True # tells if we need to print from right to left or left to right

    ans = [] # stores the answer

    while len(curr_level) != 0:
        node = curr_level.popleft() # taking the node at top

        ans.append(node.data)

        if reverse:
            # adding left first so that right child is at the start of the queue
            if node.left != None: next_level.appendleft(node.left)
            if node.right != None: next_level.appendleft(node.right)
        else:
            # adding right first so that left child is at the start of the queue
            if node.right != None: next_level.appendleft(node.right)
            if node.left != None: next_level.appendleft(node.left)
        
        if len(curr_level) == 0:
            reverse = not reverse

            curr_level, next_level = next_level, curr_level
    return ans