# Convert BST to Min Heap

# tree node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None

# inroder traversal to store the node values in sorted order


def inorder(node, arr):
    if node is None:
        return

    inorder(node.left, arr)
    arr.append(node.val)
    inorder(node.right, arr)

# preorder to update the value of the nodes


def preorder(node, idx, arr):
    if node is None:
        return

    idx[0] += 1
    node.data = arr[idx]

    preorder(node.left, idx, arr)
    preorder(node.right, idx, arr)


def convert_bst_to_min_heap(root):
    arr = []
    idx = [-1]

    # adding values to arr
    inorder(root, arr)

    # converting bst to min heap
    preorder(arr, idx, arr)

# to print the tree


def print_tree(root):
    if root is None:
        return

    print(root.data, end=" ")
    print_tree(root.left)
    print_tree(root.right)
