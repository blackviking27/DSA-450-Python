# Check for Balanced Tree

f = True # global varaible which checks if a tree is balanced or not
def solve(root):
    if root is None: return 0

    lh = solve(root.left) # height of left subtree
    rh = solve(root.right) # height of right subtree

    # if at any node the difference between left and right subtree is greater than 1
    # then the whole subtree is unbalanced
    if abs(lh - rh) > 1: 
        global f
        f = False
    return max(lh, rh) + 1 # returning the height of the sub tree

#Function to check whether a binary tree is balanced or not.
def isBalanced(root):
    global f
    f = True
    solve(root)
    return f