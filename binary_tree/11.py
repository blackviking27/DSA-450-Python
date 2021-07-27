# Bottom View of Binary Tree

from collections import deque, defaultdict
def bottomView(root):

    if root is None: return [] # if root node is none
    
    q = deque([[root, 0]]) # storing node and it's horizontal value
    mapping = defaultdict(int)
    mi = float('inf') # gives the minimum horizontal distance
    while len(q) != 0:
        node, hd = q.popleft() # remove the element at the beginning
        
        # adding the node data for current horizontal distance 
        # since we are moving from top to bottom then for each level we go down 
        # we encounter a node which is below the node at current horizontal distance
        mapping[hd] = node.data 
    
        if mi > hd: mi = hd # updating the minimum horizontal distance
    
        if node.left != None: q.append([node.left, hd - 1]) # taking the left child
        if node.right != None: q.append([node.right, hd + 1]) # taking the right child

    ans = []
    
    # moving for all the horizontal distance
    while mi in mapping:
        ans.append(mapping[mi])
        mi += 1
    return ans