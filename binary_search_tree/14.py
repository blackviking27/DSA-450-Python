# Median of BST

def noOfNodes(root, count):
    if root is None:
        return
    
    noOfNodes(root.left, count)
    count[0] += 1
    noOfNodes(root.right, count)

def find(root, curr, prev, c, k, f):
    if root is None:
        return
    
    find(root.left, curr, prev , c, k, f)
    
    if prev[0] == None:
        prev[0] = root
        c[0] += 1
    elif c[0] == k:
        c[0] += 1
        curr[0] = root
        f[0] = 1
        return
    elif f[0] == 0:
        prev[0] = root
        c[0] += 1
    
    find(root.right, curr, prev , c, k, f)
    

def findMedian(root):
    count = [0]
    noOfNodes(root, count)
    
    curr = [None]
    prev = [None]
    c = [1]
    
    # position of median
    x = (count[0] // 2) + 1
    flag = [0]
    
    find(root, curr, prev, c, x, flag)
    
    if count[0] % 2 != 0:
        return curr[0].data
    else:
        n = (curr[0].data + prev[0].data) / 2
        temp = (n * 10) % 10
        return n if temp != 0.0 else int(n)