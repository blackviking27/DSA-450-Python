# Largest BST in a Binary Tree [ V.V.V.V.V IMP ]

def solve(root):
    if root is None:
        return [1, 0, float('inf'), float('-inf')]
    
    # for leaf nodes
    if root.left is None and root.right is None:
        return [1, 1, root.data, root.data]

    # for other nodes
    l = solve(root.left)
    r = solve(root.right)
    # if both left and right subtree are BST
    if l[0] and r[0]:
        if root.data > l[3] and root.data < r[2]:
            x = l[2]
            y = r[3]
            # incase either tree was None
            if x == float('inf'): x = root.data
            if y == float('-inf'): y = root.data
            return [1, l[1] + r[1] + 1, x, y]
    
    # if not able to form a BST
    return [0, max(l[1], r[1]), 0, 0]


def largestBST(root):
    ans = solve(root)
    return ans[1]
