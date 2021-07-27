# 	Find min and max value in a BST

def min_and_max(root):
    minVal = root
    maxVal = root

    # min value    
    while minVal.left is not None:
        minVal = minVal.left
    
    # max value
    while maxVal.right is not None:
        maxVal = maxVal.right
    
    return minVal, maxVal