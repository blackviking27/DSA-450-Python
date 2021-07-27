# Find distance between two nodes of a Binary Tree

# to find the lca of the two values
def lca(root, n1, n2):
    if root is None:
        return None
    if root.data == n1 or root.data == n2: return root
    l = lca(root.left, n1, n2)
    r = lca(root.right, n1, n2)
    if l != None and r != None: return root
    if l:
        return l
    else:
        return r

# find the distance from lca node to one of the node
def dist(root, a):
    if root is None:
        return 0
    if root.data == a: return 1
    
    x = dist(root.left, a)
    y = dist(root.right, a)
    
    # if a is not present in both left and right subtree
    if not x and not y: return 0
    return x + y + 1

def findDist(root,a,b):
    lca_node = lca(root, a, b)
    dist1 = dist(lca_node, a)
    dist2 = dist(lca_node, b)
    return dist1 + dist2 - 2