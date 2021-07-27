# Replace every element with the least greater element on its right

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    
    global succ
    if key < root.data:
        succ = root
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    
    return root

def replace(arr, n):
    global succ
    root = None
    for i in range(n-1, -1, -1):
        succ = None
        root = insert(root, arr[i])

        if succ is not None:
            arr[i] = succ.data
        else:
            arr[i] = -1

    return arr

# driver code
arr = [ 8, 58, 71, 18, 31, 32, 63,
            92, 43, 3, 91, 93, 25, 80, 28 ]
n = len(arr)
succ = None
arr = replace(arr, n)

print(*arr)