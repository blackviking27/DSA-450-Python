# Print all k-sum paths in a binary tree

class newNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def k_sum_path(root, path, k):
    if root is None:
        return
    
    path.append(root.data)

    k_sum_path(root.left, path, k)
    k_sum_path(root.right, path, k)

    f = 0
    for j in range(len(path) -1, -1, -1):
        f += path[j]

        if f == k:
            global ans
            ans.append(path[j:])
    path.pop()

# Driver code
root = newNode(1) 
root.left = newNode(3) 
root.left.left = newNode(2) 
root.left.right = newNode(1) 
root.left.right.left = newNode(1) 
root.right = newNode(-1) 
root.right.left = newNode(4) 
root.right.left.left = newNode(1) 
root.right.left.right = newNode(2) 
root.right.right = newNode(5) 
root.right.right.right = newNode(2) 
  
k = 5
ans = []
path = []
k_sum_path(root, path, k)
print(*ans)
