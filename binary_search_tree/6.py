# Find LCA of 2 nodes in a BST

# iterative solution
def lca_itr(self, root, n1, n2):
    curr = root
    ans = None
    while curr is not None:
        if curr.data < n1 and curr.data < n2:
            curr = curr.right
        elif  curr.data > n1 and curr.data > n2:
            curr = curr.left
        else:
            ans = curr
            break
    return ans

# recursive solution
def lca_recur(self, root, n1, n2):
    if root is None:
        return None
    
    if root.data > n1 and root.data > n2: return lca_recur(root.left, n1, n2)
    elif root.data < n1 and root.data < n2: return lca_recur(root.right, n1, n2)
    else: return root
    