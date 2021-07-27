# Minimum swap required to convert binary tree to binary search tree

# gives the inorder traversal
def inorder(arr, n, index):
    if index >= n:
        return
    
    inorder(arr, n, 2*index + 1)
    global v
    v.append(arr[index])
    inorder(arr, n, 2*index + 2)

# min number of swaps to sort an array
def minSwaps(v):
    arrpos = [] # stores the position and array value
    n = len(v)
    for i in range(n):
        arrpos.append([v[i], i])
    
    arrpos = sorted(arrpos) # sorting the array according to value so that they are in correct position
    vis = [False for i in range(n)] # to mark if a position is visited or not
    ans = 0

    for i in range(n):
        if vis[i] or arrpos[i][1] == i:
            continue
        
        j = i
        cycle_size = 0
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][1]
            cycle_size += 1
        
        if cycle_size != 0:
            ans += (cycle_size - 1)
    return ans

# logic
# The inorder traversal of a binary search tree is in increasing order i.e it is soreted
# first find the inorder of current tree and then find min swaps required to sort it

# driver code
v = []
# a = [ 5, 6, 7, 8, 9, 10, 11 ]
a = [1, 2, 3]
n = len(a)
inorder(a, n, 0)
print(minSwaps(v))
 